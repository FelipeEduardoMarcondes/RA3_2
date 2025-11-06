# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A ↦ {tipo: int}] ⊢ (e₁ A) : int
```

---

## Linha 2

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5.5): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'B' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B ↦ {tipo: real}] ⊢ (e₁ B) : real
```

---

## Linha 3

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, real) = real
```

---

## Linha 4

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VAR_NAO_EXISTENTE): Regra 2.2 (Identificador) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(VAR_NAO_EXISTENTE).tipo = None, Γ(VAR_NAO_EXISTENTE).inicializada = true
──────────────────────────────────────────────
Γ ⊢ VAR_NAO_EXISTENTE : None
```

---

## Linha 5

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3.0): Regra 2.1 (Literal) -> real
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** int == int, real == int

---

## Linha 6

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.0): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : None
```
**Restrição:** real == int, int == int

---

## Linha 7

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 1.5): Regra 2.1 (Literal) -> real
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** real == int, e₂.valor > 0

---

## Linha 8

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: -2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 9

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 10

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, real) -> booleano
4. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (booleano, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(booleano, int) = None
```

---

## Linha 11

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 12

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: RESULTADO_BOOL): Regra 2.2 (Identificador) -> None
2. Nó 'id' (Valor: FLAG): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'None' em 'FLAG' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : None    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FLAG ↦ {tipo: None}] ⊢ (e₁ FLAG) : None
```

---

## Linha 13

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: FLAG): Regra 2.2 (Identificador) -> None
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (None, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** None == int, int == int

---

## Linha 14

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
4. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:int, then:int, else:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** int == booleano, int == int

---

## Linha 15

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
4. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:int, then:int, else:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** int == booleano, int == int

---

## Linha 16

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> ERRO
4. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:real, body:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : None
```
**Restrição:** real == booleano

---

## Linha 17

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 1.5): Regra 2.1 (Literal) -> real
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : real
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** booleano == booleano, int == real

---

## Linha 18

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 5.5): Regra 2.1 (Literal) -> real
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (real, real) -> booleano
4. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : real
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** booleano == booleano, int == real

---

## Linha 19

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, int) -> booleano
7. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
8. Nó 'num' (Valor: 2.0): Regra 2.1 (Literal) -> real
9. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:real) -> None
10. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
11. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:None, else:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : None    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** booleano == booleano, None == int

---

## Linha 20

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1.5): Regra 2.1 (Literal) -> real
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='real' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : real    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = 1.5

---

## Linha 21

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = 0

---

## Linha 22

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -10): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = -10

---

## Linha 23

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 99999): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = 99999

---

## Linha 24

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = A

---

## Linha 25

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** int == int, int == int

---

## Linha 26

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 0.0): Regra 2.1 (Literal) -> real
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, real) = None
```

---

## Linha 27

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'ZER' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[ZER ↦ {tipo: int}] ⊢ (e₁ ZER) : int
```

---

## Linha 28

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 29

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, int) = real
```

---

## Linha 30

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
6. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
7. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
8. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 31

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1.0): Regra 2.1 (Literal) -> real
5. Nó 'num' (Valor: 100.0): Regra 2.1 (Literal) -> real
6. Nó 'id' (Valor: ZER): Regra 2.2 (Identificador) -> int
7. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, int) -> real
8. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:real, else:real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : real    Γ ⊢ e₃ : real
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : real
```
**Restrições:** booleano == booleano, real == real

---

## Linha 32

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 1 : int
```

---

## Linha 33

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 2 : int
```

---

## Linha 34

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 3 : int
```

---

## Linha 35

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 4 : int
```

---

## Linha 36

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 5 : int
```

---

## Linha 37

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 6): Regra 2.1 (Literal) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.1: Literal**
```
Γ ⊢ 6 : int
```

---

## Linha 38

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
3. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
4. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
7. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
8. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 39

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
3. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
4. Nó 'num' (Valor: 2.0): Regra 2.1 (Literal) -> real
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, real) -> real
7. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
8. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, int) = real
```

