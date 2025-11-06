# FELIPE EDUARDO MARCONDES
# GRUPO 2
# Compilador completo: Analisadores Léxico + Sintático + Semântico

import sys
import json
import io
import os
from leitor import lerTokens
from parser import parsear, construirGramatica, calcularFirst, calcularFollow, construirTabelaLL1
from semantico import (
    criarTabelaSimbolos, 
    definirGramaticaAtributos,
    analisarSemantica,
    gerarArvoreAtribuida,
    gerarRelatorioTipos,
    gerarRelatorioErros
)


def imprimirArvore(node, indent=0, prefix=""):
    # Imprime a árvore sintática de forma hierárquica.
    if node is None:
        return
    
    tipo_info = ""
    if 'tipo_inferido' in node and node['tipo_inferido']:
        tipo_info = f" : {node['tipo_inferido']}"
    
    print("  " * indent + prefix + node['type'] + tipo_info, end="")

    if node['value'] is not None:
        print(f" = {node['value']}")
    else:
        print()

    for i, child in enumerate(node.get('children', [])):
        is_last = (i == len(node['children']) - 1)
        child_prefix = "└─ " if is_last else "├─ "
        imprimirArvore(child, indent + 1, child_prefix)


def gerarGramaticaAtributosMd(gramatica_atributos, filename='analises/gramatica_atributos.md'):
    # Gera arquivo markdown completo com a gramática de atributos
    
    descricao = gramatica_atributos.get('descricao', "Gramática de Atributos RPN")
    regras = gramatica_atributos.get('regras_tipo', {})

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("# Gramática de Atributos - Linguagem RPN\n\n")
        f.write("**Gerado automaticamente pelo compilador (Versão Completa)**\n\n")
        
        f.write("## 1. Atributos\n\n")
        f.write(descricao)
        f.write("\n\n")
        
        f.write("## 2. Regras de Produção com Atributos\n\n")
        f.write("Para cada nó da árvore, calculamos os seguintes atributos **sintetizados**:\n")
        f.write("- **tipo**: {int, real, booleano}\n")
        f.write("- **valor**: Valor computado (se aplicável)\n")
        
        f.write("\n---\n\n")
        
        f.write("### 2.1 Literais (EXPR -> num)\n\n")
        f.write("- **Regra:** `Γ ⊢ num : int` (se `num` é inteiro); `Γ ⊢ num : real` (se `num` tem ponto decimal)\n")
        f.write("- **RPN:** `(5)` -> `tipo: int` | `(5.0)` -> `tipo: real`\n")
        f.write("- **Sintetizado:** `EXPR.tipo` = `int` ou `real`\n")

        f.write("\n---\n\n")

        f.write("### 2.2 Identificadores (EXPR -> id)\n\n")
        f.write("- **Regra:** `Γ(x) = T, Γ(x).inicializada = true ──────────────── Γ ⊢ x : T`\n")
        f.write("- **RPN:** `(X)` -> `tipo: Γ(X).tipo`\n")
        f.write("- **Sintetizado:** `EXPR.tipo` = `TabelaSimbolos[id.nome].tipo`\n")
        f.write("- **Restrição:** ERRO se `id.nome` não inicializado.\n")

        f.write("\n---\n\n")
        
        f.write("### 2.3 Operações Aritméticas (STMT -> EXPR₁ EXPR₂ op_bin) (op ∈ {+, -, *, |})\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂ ──────────────── Γ ⊢ (e₁ e₂ op) : promover_tipo(T₁, T₂)`\n")
        f.write("- **RPN:** `(3.0 5 +)` -> `tipo: real`\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `promover_tipo(EXPR₁.tipo, EXPR₂.tipo)`.\n")
        f.write("- **Restrição:** ERRO se `T₁` ou `T₂` for `booleano`.\n")
        
        f.write("\n---\n\n")

        f.write("### 2.4 Divisão Inteira/Módulo (STMT -> EXPR₁ EXPR₂ op_bin) (op ∈ {/, %})\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : int, Γ ⊢ e₂ : int, e₂.valor ≠ 0 ──────────────── Γ ⊢ (e₁ e₂ op) : int`\n")
        f.write("- **RPN:** `(10 3 /)` -> `tipo: int`\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `int`\n")
        f.write("- **Restrição:** ERRO se `EXPR₁.tipo ≠ int` ou `EXPR₂.tipo ≠ int`.\n")

        f.write("\n---\n\n")

        f.write("### 2.5 Potenciação (STMT -> EXPR₁ EXPR₂ pow)\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : T, Γ ⊢ e₂ : int, e₂.valor > 0 ──────────────── Γ ⊢ (e₁ e₂ ^) : T`\n")
        f.write("- **RPN:** `(2.0 3 ^)` -> `tipo: real`\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `EXPR₁.tipo`\n")
        f.write("- **Restrição:** ERRO se `EXPR₂.tipo ≠ int` ou `EXPR₂.valor ≤ 0`.\n")

        f.write("\n---\n\n")

        f.write("### 2.6 Operadores Relacionais (STMT -> EXPR₁ EXPR₂ op_rel)\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : T₁, Γ ⊢ e₂ : T₂, T₁,T₂ ∈ {int, real} ──────────────── Γ ⊢ (e₁ e₂ op) : booleano`\n")
        f.write("- **RPN:** `(X 10 <)` -> `tipo: booleano`\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `booleano`\n")
        f.write("- **Restrição:** ERRO se `T₁` ou `T₂` ∉ `{int, real}`.\n")

        f.write("\n---\n\n")

        f.write("### 2.7 Armazenamento (STMT -> EXPR id)\n\n")
        f.write("- **Regra:** `Γ ⊢ e : T, T ∈ {int, real} ──────────────── Γ[id ↦ {tipo:T}] ⊢ (e id) : T`\n")
        f.write("- **RPN:** `(42 X)` -> `tipo: int` (Efeito colateral: atualiza `Γ(X)`)\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `EXPR.tipo`\n")
        f.write("- **Restrição:** ERRO se `EXPR.tipo = booleano`.\n")

        f.write("\n---\n\n")

        f.write("### 2.8 Histórico (STMT -> EXPR res)\n\n")
        f.write("- **Regra:** `Γ ⊢ e : int, e.valor ≥ 1, ... ──────────────── Γ ⊢ (e RES) : T` (onde T = tipo da linha referenciada)\n")
        f.write("- **RPN:** `(1 RES)` -> `tipo: T` (tipo da linha anterior)\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `historico[tamanho - EXPR.valor].tipo`\n")
        f.write("- **Restrição:** ERRO se `EXPR.tipo ≠ int` ou `EXPR.valor < 1`.\n")

        f.write("\n---\n\n")

        f.write("### 2.9 Condicional (STMT -> EXPR₁ EXPR₂ EXPR₃ if)\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : booleano, Γ ⊢ e₂ : T, Γ ⊢ e₃ : T ──────────────── Γ ⊢ (e₁ e₂ e₃ if) : T`\n")
        f.write("- **RPN:** `((X 0 >) (1) (0) if)` -> `tipo: int`\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `EXPR₂.tipo`\n")
        f.write("- **Restrição:** ERRO se `EXPR₁.tipo ≠ booleano` ou `EXPR₂.tipo ≠ EXPR₃.tipo`.\n")

        f.write("\n---\n\n")

        f.write("### 2.10 Laço (STMT -> EXPR₁ EXPR₂ while)\n\n")
        f.write("- **Regra:** `Γ ⊢ e₁ : booleano, Γ ⊢ e₂ : T ──────────────── Γ ⊢ (e₁ e₂ while) : T`\n")
        f.write("- **RPN:** `((I 10 <) ((I 1 +) I) while)` -> `tipo: int` (tipo do corpo `T`)\n")
        f.write("- **Sintetizado:** `STMT.tipo` = `EXPR₂.tipo`\n")
        f.write("- **Restrição:** ERRO se `EXPR₁.tipo ≠ booleano`.\n")
        
        f.write("\n---\n\n")

        f.write("## 3. Tabela de Operadores (Extraída de `definirGramaticaAtributos`)\n\n")
        f.write("| Operador | Função de Tipo |\n")
        f.write("|----------|----------------|\n")
        
        for op, func in regras.items():
            if op in ['plus', 'minus', 'mult', 'div_real']:
                f.write(f"| `{op}` | promover_tipo(T₁, T₂) |\n")

            elif op == 'div_int':
                f.write(f"| `{op}` | int se T₁=int ∧ T₂=int |\n")

            elif op == 'mod':
                f.write(f"| `{op}` | int se T₁=int ∧ T₂=int |\n")
                
            elif op == 'pow':
                f.write(f"| `{op}` | T₁ se T₂=int |\n")

            elif op in ['lt', 'gt', 'lte', 'gte', 'eq', 'neq']:
                f.write(f"| `{op}` | booleano se T₁,T₂ ∈ {{int,real}} |\n")

def main():
    if len(sys.argv) != 2:
        print("=" * 60)
        print("COMPILADOR RPN - Fases 1, 2 e 3")
        print("=" * 60)
        print("\nUso: python compilar.py <arquivo.txt>")
        print("\nExemplo: python compilar.py teste1.txt")
        print("=" * 60)
        sys.exit(1)
    
    filename = sys.argv[1]
    
    output_dir = 'analises'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    base_name = os.path.splitext(os.path.basename(filename))[0]
    
    gramatica_file = os.path.join(output_dir, 'gramatica_atributos_gerada.md')
    relatorio_tipos_file = os.path.join(output_dir, f"{base_name}_julgamento_tipos.md")
    relatorio_erros_file = os.path.join(output_dir, f"{base_name}_erros_semanticos.md")
    arvore_json_file = os.path.join(output_dir, f"{base_name}_arvore_atribuida.json")
    arvore_md_file = os.path.join(output_dir, f"{base_name}_arvore_sintatica.md")
    
    try:
        print("=" * 60)
        print(f"COMPILANDO: {filename}")
        print("=" * 60)
        
        # ========== FASE 1: ANÁLISE LÉXICA ==========
        print("\n[FASE 1] Análise Léxica...")
        tokens = lerTokens(filename)
        num_tokens = len([t for t in tokens if t['type'] != 'eof'])
        print(f"{num_tokens} token(s) identificado(s)")
        
        # ========== FASE 2: ANÁLISE SINTÁTICA ==========
        print("\n[FASE 2] Análise Sintática...")
        gramatica = construirGramatica()
        first = calcularFirst(gramatica)
        follow = calcularFollow(gramatica, first)
        tabela_ll1 = construirTabelaLL1(gramatica, first, follow)
        
        ast_list, erros_sintaticos = parsear(tokens, tabela_ll1)
        
        if erros_sintaticos:
            print(f"{len(erros_sintaticos)} erro(s) sintático(s) encontrado(s):")
            for erro in erros_sintaticos:
                print(f"  - {erro}")
            print("\nCompilação interrompida devido a erros sintáticos.")
            sys.exit(1)
        
        print(f"{len(ast_list)} expressão(ões) válida(s)")
        
        # ========== FASE 3: ANÁLISE SEMÂNTICA ==========
        print("\n[FASE 3] Análise Semântica...")
        
        gramatica_atributos = definirGramaticaAtributos()
        
        tabela_simbolos = criarTabelaSimbolos() # MUDANÇA: Usa a função camelCase
        arvore_anotada, erros_semanticos = analisarSemantica(ast_list, tabela_simbolos)
        
        if erros_semanticos:
            print(f"{len(erros_semanticos)} erro(s) semântico(s) encontrado(s):\n")
            for erro in erros_semanticos:
                print(erro)
            print("\nCompilação concluída com erros semânticos.")

        else:
            print("Nenhum erro semântico detectado")
        
        print("\n[FASE 3.1] Gerando árvore atribuída...")
        arvore_atribuida_final = gerarArvoreAtribuida(arvore_anotada)
        print("Árvore sintática abstrata atribuída gerada")
        
        # ========== GERAÇÃO DE RELATÓRIOS ==========
        print("\n[SAÍDA] Gerando relatórios...")
        
        gerarGramaticaAtributosMd(gramatica_atributos, gramatica_file)
        print(f"{gramatica_file} (estático)")
        
        gerarRelatorioTipos(arvore_anotada, relatorio_tipos_file)
        print(f"{relatorio_tipos_file}")
        
        gerarRelatorioErros(erros_semanticos, relatorio_erros_file)
        print(f"{relatorio_erros_file}")
        
        with open(arvore_json_file, 'w', encoding='utf-8') as f:
            json.dump(arvore_atribuida_final, f, indent=2, ensure_ascii=False)
        print(f"{arvore_json_file}")
        
        with open(arvore_md_file, 'w', encoding='utf-8') as f:
            f.write(f"# Árvore Sintática Atribuída - {filename}\n\n")
            f.write("**Gerado pelo compilador RPN - Fase 3**\n\n")
            
            for linha_num, ast in arvore_anotada:
                f.write(f"## Expressão {linha_num}\n\n")
                f.write(f"**Tipo inferido:** `{ast.get('tipo_inferido', 'ERRO')}`\n\n")
                f.write("```\n")
                
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                imprimirArvore(ast)
                output = buffer.getvalue()
                sys.stdout = old_stdout
                
                f.write(output)
                f.write("```\n\n")
        print(f"{arvore_md_file}")
        
        print("\n" + "=" * 60)
        print("RESUMO DA COMPILAÇÃO")
        print("=" * 60)
        print(f"Tokens processados:      {num_tokens}")
        print(f"Expressões analisadas:   {len(ast_list)}")
        print(f"Variáveis declaradas:    {len(tabela_simbolos['simbolos'])}") 
        print(f"Histórico de resultados: {len(tabela_simbolos['historico'])}")
        print(f"Erros semânticos:        {len(erros_semanticos)}")
        
        if erros_semanticos:
            print("\nStatus: COMPILAÇÃO CONCLUÍDA COM ERROS")
            print("=" * 60)
            sys.exit(1)
        else:
            print("\nStatus: COMPILAÇÃO BEM-SUCEDIDA")
        
        print("=" * 60)
        
        print("\n[ÁRVORES SINTÁTICAS ATRIBUÍDAS]")
        print("=" * 60)
        
        for linha_num, ast in arvore_anotada:
            print(f"\n--- Expressão {linha_num} (Tipo: {ast.get('tipo_inferido', 'ERRO')}) ---")
            imprimirArvore(ast)
            print("-" * 60)
        

        if tabela_simbolos['simbolos']: 
            print("\n[TABELA DE SÍMBOLOS]")
            print("=" * 60)
            print(f"{'Identificador':<20} {'Tipo':<10} {'Linha':<10} {'Inicializada'}")
            print("-" * 60)
            
            for nome, info in sorted(tabela_simbolos['simbolos'].items()):
                inicializada = "Sim" if info['inicializada'] else "Não"
                print(f"{nome:<20} {info['tipo']:<10} {info['linha']:<10} {inicializada}")
            
            print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"\nERRO: Arquivo não encontrado - {e}")
        sys.exit(1)
        
    except SyntaxError as e:
        print(f"\nERRO DE SINTAXE: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"\nERRO DE VALOR: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"\nERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()