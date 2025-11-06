# Relatório de Julgamento de Tipos

Análise detalhada da inferência de tipos e aplicação das regras semânticas (Gramática de Atributos) para cada linha de expressão.

---

## Linha 1

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.428676643235324): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'A' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A ↦ {tipo: real}] ⊢ (e₁ A) : real
```

---

## Linha 2

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 20.53): Regra 2.1 (Literal) -> real
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

1. Nó 'num' (Valor: -5.345345): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'C' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[C ↦ {tipo: real}] ⊢ (e₁ C) : real
```

---

## Linha 4

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (real, real) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** real, real ∈ {int, real}

---

## Linha 5

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (real, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <=) : booleano
```
**Restrição:** real, int ∈ {int, real}

---

## Linha 6

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='real' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : real    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = B

---

## Linha 7

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (real, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** real, int ∈ {int, real}

---

## Linha 8

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: -5): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (real, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** real, int ∈ {int, real}

---

## Linha 9

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (real, real) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ !=) : booleano
```
**Restrição:** real, real ∈ {int, real}

---

## Linha 10

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 11

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, real) = real
```

---

## Linha 12

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 13

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
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

## Linha 14

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7.0): Regra 2.1 (Literal) -> real
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, real) = real
```

---

## Linha 15

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 16

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 8): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 17

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (real, real) -> booleano
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (real, int) -> booleano
7. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
8. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
9. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
10. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
11. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 18

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 19

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 20

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 2

---

## Linha 21

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 22

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, int) -> real
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, real) = real
```

---

## Linha 23

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, real) = real
```

---

## Linha 24

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, real) -> None
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
7. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (None, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : None
```
**Restrição:** None, real ∈ {int, real}

---

## Linha 25

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 26

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, real) = real
```

---

## Linha 27

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'X' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[X ↦ {tipo: int}] ⊢ (e₁ X) : int
```

---

## Linha 28

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 200): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Y' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Y ↦ {tipo: int}] ⊢ (e₁ Y) : int
```

---

## Linha 29

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -50.5): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'Z' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Z ↦ {tipo: real}] ⊢ (e₁ Z) : real
```

---

## Linha 30

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 31

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(I).tipo = int, Γ(I).inicializada = true
──────────────────────────────────────────────
Γ ⊢ I : int
```

---

## Linha 32

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, int) -> booleano
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, int) -> booleano
7. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
8. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
9. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
10. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
11. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:real, else:int) -> None
12. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
13. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:None, else:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : None    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** booleano == booleano, None == int

---

## Linha 33

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: RAIO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'RAIO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[RAIO ↦ {tipo: int}] ⊢ (e₁ RAIO) : int
```

---

## Linha 34

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'PI' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PI ↦ {tipo: int}] ⊢ (e₁ PI) : int
```

---

## Linha 35

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: LIMIT): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'LIMIT' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[LIMIT ↦ {tipo: int}] ⊢ (e₁ LIMIT) : int
```

---

## Linha 36

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: VALORANTIGO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'VALORANTIGO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[VALORANTIGO ↦ {tipo: int}] ⊢ (e₁ VALORANTIGO) : int
```

---

## Linha 37

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: RESULTADO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'RESULTADO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[RESULTADO ↦ {tipo: int}] ⊢ (e₁ RESULTADO) : int
```

---

## Linha 38

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: RAIO): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: RAIO): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: LIMIT): Regra 2.2 (Identificador) -> int
7. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
8. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
9. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
10. Nó 'id' (Valor: VALORANTIGO): Regra 2.2 (Identificador) -> int
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'id' (Valor: RESULTADO): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'RESULTADO' -> int
14. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
15. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
16. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
17. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
18. Nó 'id' (Valor: RAIO): Regra 2.2 (Identificador) -> int
19. Nó 'id' (Valor: RAIO): Regra 2.2 (Identificador) -> int
20. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
21. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> int
22. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
23. Nó 'id' (Valor: LIMIT): Regra 2.2 (Identificador) -> int
24. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
25. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
26. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int
27. Nó 'id' (Valor: VALORANTIGO): Regra 2.2 (Identificador) -> int
28. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
29. Nó 'id' (Valor: RESULTADO): Regra 2.2 (Identificador) -> None
30. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'RESULTADO' -> int
31. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
32. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
33. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
34. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
35. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 39

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'D' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[D ↦ {tipo: int}] ⊢ (e₁ D) : int
```

---

## Linha 40

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'E' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[E ↦ {tipo: int}] ⊢ (e₁ E) : int
```

---

## Linha 41

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'F' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[F ↦ {tipo: int}] ⊢ (e₁ F) : int
```

---

## Linha 42

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: G): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'G' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[G ↦ {tipo: int}] ⊢ (e₁ G) : int
```

---

## Linha 43

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: H): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'H' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[H ↦ {tipo: int}] ⊢ (e₁ H) : int
```

---

## Linha 44

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: J): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'J' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[J ↦ {tipo: int}] ⊢ (e₁ J) : int
```

---

## Linha 45

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: K): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'K' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[K ↦ {tipo: int}] ⊢ (e₁ K) : int
```

---

## Linha 46

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: L): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'L' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[L ↦ {tipo: int}] ⊢ (e₁ L) : int
```

---

## Linha 47

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'M' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[M ↦ {tipo: int}] ⊢ (e₁ M) : int
```

---

## Linha 48

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[N ↦ {tipo: int}] ⊢ (e₁ N) : int
```

---

## Linha 49

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: O): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'O' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[O ↦ {tipo: int}] ⊢ (e₁ O) : int
```

---

## Linha 50

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: P): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'P' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[P ↦ {tipo: int}] ⊢ (e₁ P) : int
```

---

## Linha 51

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Q): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Q' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Q ↦ {tipo: int}] ⊢ (e₁ Q) : int
```

---

## Linha 52

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: R): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'R' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[R ↦ {tipo: int}] ⊢ (e₁ R) : int
```

---

## Linha 53

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: S): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'S' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[S ↦ {tipo: int}] ⊢ (e₁ S) : int
```

---

## Linha 54

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: T): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'T' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[T ↦ {tipo: int}] ⊢ (e₁ T) : int
```

---

## Linha 55

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: U): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'U' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[U ↦ {tipo: int}] ⊢ (e₁ U) : int
```

---

## Linha 56

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
7. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, real) = real
```

---

## Linha 57

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
8. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> int
9. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
10. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
11. Nó 'id' (Valor: G): Regra 2.2 (Identificador) -> int
12. Nó 'id' (Valor: H): Regra 2.2 (Identificador) -> int
13. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
14. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
15. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real
16. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
17. Nó 'id' (Valor: J): Regra 2.2 (Identificador) -> int
18. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
19. Nó 'id' (Valor: K): Regra 2.2 (Identificador) -> int
20. Nó 'id' (Valor: L): Regra 2.2 (Identificador) -> int
21. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
22. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
23. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, int) -> real
24. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> int
25. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
26. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
27. Nó 'id' (Valor: O): Regra 2.2 (Identificador) -> int
28. Nó 'id' (Valor: P): Regra 2.2 (Identificador) -> int
29. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
30. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
31. Nó 'id' (Valor: Q): Regra 2.2 (Identificador) -> int
32. Nó 'id' (Valor: R): Regra 2.2 (Identificador) -> int
33. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
34. Nó 'id' (Valor: S): Regra 2.2 (Identificador) -> int
35. Nó 'id' (Valor: T): Regra 2.2 (Identificador) -> int
36. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
37. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
38. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
39. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, int) = real
```

---

## Linha 58

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: ZERO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'ZERO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[ZERO ↦ {tipo: int}] ⊢ (e₁ ZERO) : int
```

---

## Linha 59

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: UM): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'UM' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[UM ↦ {tipo: int}] ⊢ (e₁ UM) : int
```

---

## Linha 60

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: DEZ): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'DEZ' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[DEZ ↦ {tipo: int}] ⊢ (e₁ DEZ) : int
```

---

## Linha 61

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: CEM): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CEM' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CEM ↦ {tipo: int}] ⊢ (e₁ CEM) : int
```

---

## Linha 62

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: NEGATIVO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'NEGATIVO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[NEGATIVO ↦ {tipo: int}] ⊢ (e₁ NEGATIVO) : int
```

---

## Linha 63

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: MEIO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'MEIO' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MEIO ↦ {tipo: real}] ⊢ (e₁ MEIO) : real
```

---

## Linha 64

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1000): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: MIL): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'MIL' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MIL ↦ {tipo: int}] ⊢ (e₁ MIL) : int
```

---

## Linha 65

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3.14159265359): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'PI' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PI ↦ {tipo: real}] ⊢ (e₁ PI) : real
```

---

## Linha 66

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (real, real) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 67

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (real, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 68

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: J): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'J' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[J ↦ {tipo: int}] ⊢ (e₁ J) : int
```

---

## Linha 69

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 70

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 15): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
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

## Linha 71

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 2.5): Regra 2.1 (Literal) -> real
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, real) = real
```

---

## Linha 72

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 73

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 8): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : int
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 74

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 75

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 76

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 77

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, int) = real
```

---

## Linha 78

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
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

## Linha 79

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (real, real) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** real, real ∈ {int, real}

---

## Linha 80

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 81

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 82

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: P): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Q): Regra 2.2 (Identificador) -> int
3. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ !=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 83

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: R): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: S): Regra 2.2 (Identificador) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 84

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: T): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: U): Regra 2.2 (Identificador) -> int
3. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 85

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, real) = real
```

---

## Linha 86

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 87

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: G): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: H): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 88

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 42): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'X' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[X ↦ {tipo: int}] ⊢ (e₁ X) : int
```

---

## Linha 89

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Y' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Y ↦ {tipo: int}] ⊢ (e₁ Y) : int
```

---

## Linha 90

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> None
5. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'Z' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Z ↦ {tipo: real}] ⊢ (e₁ Z) : real
```

---

## Linha 91

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 92

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:real, else:real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : real    Γ ⊢ e₃ : real
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : real
```
**Restrições:** booleano == booleano, real == real

---

## Linha 93

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 45.6866): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : real
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 94

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'VALOR' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[VALOR ↦ {tipo: int}] ⊢ (e₁ VALOR) : int
```

---

## Linha 95

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 96

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 180): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** real == int, int == int

---

## Linha 97

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: METROS): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'METROS' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[METROS ↦ {tipo: int}] ⊢ (e₁ METROS) : int
```

---

## Linha 98

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: METROS): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 3.28084): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 99

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: POLEGADAS): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'POLEGADAS' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[POLEGADAS ↦ {tipo: int}] ⊢ (e₁ POLEGADAS) : int
```

---

## Linha 100

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: POLEGADAS): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2.54): Regra 2.1 (Literal) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 101

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 102

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: W): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'W' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[W ↦ {tipo: int}] ⊢ (e₁ W) : int
```

---

## Linha 103

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: W): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, real) = real
```

---

## Linha 104

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: M): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: O): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: P): Regra 2.2 (Identificador) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 105

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 106

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 107

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: MIN): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'MIN' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MIN ↦ {tipo: int}] ⊢ (e₁ MIN) : int
```

---

## Linha 108

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'MAX' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MAX ↦ {tipo: int}] ⊢ (e₁ MAX) : int
```

---

## Linha 109

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: MIN): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: MIN): Regra 2.2 (Identificador) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 110

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: MEDIA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'MEDIA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[MEDIA ↦ {tipo: int}] ⊢ (e₁ MEDIA) : int
```

---

## Linha 111

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: DESVIO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'DESVIO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[DESVIO ↦ {tipo: int}] ⊢ (e₁ DESVIO) : int
```

---

## Linha 112

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: MEDIA): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: DESVIO): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 113

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 114

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
5. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 115

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A11): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A11' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A11 ↦ {tipo: int}] ⊢ (e₁ A11) : int
```

---

## Linha 116

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B11): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B11' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B11 ↦ {tipo: int}] ⊢ (e₁ B11) : int
```

---

## Linha 117

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A12): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A12' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A12 ↦ {tipo: int}] ⊢ (e₁ A12) : int
```

---

## Linha 118

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B21): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B21' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B21 ↦ {tipo: int}] ⊢ (e₁ B21) : int
```

---

## Linha 119

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A21): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A21' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A21 ↦ {tipo: int}] ⊢ (e₁ A21) : int
```

---

## Linha 120

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B12): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B12' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B12 ↦ {tipo: int}] ⊢ (e₁ B12) : int
```

---

## Linha 121

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: A22): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'A22' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[A22 ↦ {tipo: int}] ⊢ (e₁ A22) : int
```

---

## Linha 122

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B22): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B22' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B22 ↦ {tipo: int}] ⊢ (e₁ B22) : int
```

---

## Linha 123

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A11): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B11): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: A12): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B21): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 124

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A21): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B12): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: A22): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: B22): Regra 2.2 (Identificador) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 125

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> real
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, real) -> real
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, real) = real
```

---

## Linha 126

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: TOTAL): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'TOTAL' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[TOTAL ↦ {tipo: int}] ⊢ (e₁ TOTAL) : int
```

---

## Linha 127

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: TOTAL): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 128

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, real) -> real
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** real == int, int == int

---

## Linha 129

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: CELSIUS): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CELSIUS' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CELSIUS ↦ {tipo: int}] ⊢ (e₁ CELSIUS) : int
```

---

## Linha 130

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CELSIUS): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 9): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 131

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: FAHRENHEIT): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'FAHRENHEIT' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FAHRENHEIT ↦ {tipo: int}] ⊢ (e₁ FAHRENHEIT) : int
```

---

## Linha 132

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: FAHRENHEIT): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 32): Regra 2.1 (Literal) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 133

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[SOMA ↦ {tipo: int}] ⊢ (e₁ SOMA) : int
```

---

## Linha 134

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
5. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[SOMA ↦ {tipo: int}] ⊢ (e₁ SOMA) : int
```

---

## Linha 135

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: PRODUTO): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'PRODUTO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PRODUTO ↦ {tipo: int}] ⊢ (e₁ PRODUTO) : int
```

---

## Linha 136

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PRODUTO): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: PRODUTO): Regra 2.2 (Identificador) -> None
5. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'PRODUTO' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PRODUTO ↦ {tipo: int}] ⊢ (e₁ PRODUTO) : int
```

---

## Linha 137

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: MAX): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 138

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: MIN): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: MIN): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 139

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: VALOR): Regra 2.2 (Identificador) -> int
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

## Linha 140

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:int, then:int, else:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : None
```
**Restrições:** int == booleano, int == int

---

## Linha 141

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'X' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[X ↦ {tipo: int}] ⊢ (e₁ X) : int
```

---

## Linha 142

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Y' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Y ↦ {tipo: int}] ⊢ (e₁ Y) : int
```

---

## Linha 143

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 25): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'Z' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[Z ↦ {tipo: int}] ⊢ (e₁ Z) : int
```

---

## Linha 144

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3.14159): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'PI' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[PI ↦ {tipo: real}] ⊢ (e₁ PI) : real
```

---

## Linha 145

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2.71828): Regra 2.1 (Literal) -> real
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'real' em 'E' -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : real    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[E ↦ {tipo: real}] ⊢ (e₁ E) : real
```

---

## Linha 146

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : int
```
Contexto: N = 4

---

## Linha 147

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 148

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 149

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 150

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
5. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : real
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 151

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
4. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, real) = real
```

---

## Linha 152

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 153

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 154

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
4. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
7. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >=) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 155

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (real, real) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 156

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 157

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 158

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 1001.445452112): Regra 2.1 (Literal) -> real
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, real) -> None
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (None, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : None
```
**Restrição:** None, int ∈ {int, real}

---

## Linha 159

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 160

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
5. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 161

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : int
```
**Restrição:** int == int, int == int

---

## Linha 162

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 3.7557): Regra 2.1 (Literal) -> real
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, real) -> None
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2.3345): Regra 2.1 (Literal) -> real
6. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, real) -> real
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(None, real) = None
```

---

## Linha 163

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
6. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, real) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, real) = real
```

---

## Linha 164

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
6. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 165

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100.54): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None
4. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(None, real) = None
```

---

## Linha 166

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(real, int) = real
```

---

## Linha 167

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 50): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
8. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
9. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
10. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 168

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
3. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 169

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
6. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 170

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
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

## Linha 171

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
5. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
6. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
7. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
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

## Linha 172

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 173

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 174

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(I).tipo = int, Γ(I).inicializada = true
──────────────────────────────────────────────
Γ ⊢ I : int
```

---

## Linha 175

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONTADOR' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[CONTADOR ↦ {tipo: int}] ⊢ (e₁ CONTADOR) : int
```

---

## Linha 176

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'CONTADOR' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 177

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: CONTADOR): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(CONTADOR).tipo = int, Γ(CONTADOR).inicializada = true
──────────────────────────────────────────────
Γ ⊢ CONTADOR : int
```

---

## Linha 178

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 179

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 180

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 181

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, int) -> real
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(real, int) = real
```

---

## Linha 182

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 183

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
9. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** real == int, e₂.valor > 0

---

## Linha 184

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 185

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None
8. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
9. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
10. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
11. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (None, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(None, booleano) = None
```

---

## Linha 186

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gte' (Valor: >=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 187

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'neq' (Valor: !=): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 188

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 189

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
9. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
10. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
11. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 190

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None
6. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
7. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
8. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real
9. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
10. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, None) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : None
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(None, None) = None
```

---

## Linha 191

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 192

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
6. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 193

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, int) -> None
6. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
7. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
8. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
9. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
10. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, int) -> None
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (None, None) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : None
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(None, None) = None
```

---

## Linha 194

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None
8. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
9. Nó 'eq' (Valor: ==): Regra 2.6 (Relacional) com (None, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ==) : None
```
**Restrição:** None, int ∈ {int, real}

---

## Linha 195

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
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

## Linha 196

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'B' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[B ↦ {tipo: int}] ⊢ (e₁ B) : int
```

---

## Linha 197

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'C' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[C ↦ {tipo: int}] ⊢ (e₁ C) : int
```

---

## Linha 198

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 4): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'D' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[D ↦ {tipo: int}] ⊢ (e₁ D) : int
```

---

## Linha 199

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'F' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[F ↦ {tipo: int}] ⊢ (e₁ F) : int
```

---

## Linha 200

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
9. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 201

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
9. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 202

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
8. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
9. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 203

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
8. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
9. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 204

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
6. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
8. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
9. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
10. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
11. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 205

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
6. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
8. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
9. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
10. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
11. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
12. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
13. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int
14. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
15. Nó 'if' (Valor: if): Regra 2.9 (Condicional) com (cond:booleano, then:int, else:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.9: Condicional**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int    Γ ⊢ e₃ : int
─────────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ e₃ if) : int
```
**Restrições:** booleano == booleano, int == int

---

## Linha 206

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 207

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 208

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 6): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 209

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 22): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 210

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 355): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 113): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (int, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(int, int) = real
```

---

## Linha 211

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 212

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
4. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
5. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 213

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
5. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ <) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 214

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 215

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 216

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 217

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 218

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[N ↦ {tipo: int}] ⊢ (e₁ N) : int
```

---

## Linha 219

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'N' -> int
9. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 220

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: N): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(N).tipo = int, Γ(N).inicializada = true
──────────────────────────────────────────────
Γ ⊢ N : int
```

---

## Linha 221

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[SOMA ↦ {tipo: int}] ⊢ (e₁ SOMA) : int
```

---

## Linha 222

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[I ↦ {tipo: int}] ⊢ (e₁ I) : int
```

---

## Linha 223

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
2. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
3. Nó 'lte' (Valor: <=): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
6. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
7. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> None
8. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'SOMA' -> int
9. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> int
10. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'id' (Valor: I): Regra 2.2 (Identificador) -> None
13. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'I' -> int
14. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
15. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:booleano, body:int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : int
```
**Restrição:** booleano == booleano

---

## Linha 224

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: SOMA): Regra 2.2 (Identificador) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(SOMA).tipo = int, Γ(SOMA).inicializada = true
──────────────────────────────────────────────
Γ ⊢ SOMA : int
```

---

## Linha 225

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(int, int) = int
```

---

## Linha 226

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 227

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'num' (Valor: 100): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 7): Regra 2.1 (Literal) -> int
6. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(int, int) = int
```

---

## Linha 228

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
4. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 229

**Tipo Inferido Final:** `real`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, real) -> real
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (real, int) -> real

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(real, int) = real
```

---

## Linha 230

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 231

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 20): Regra 2.1 (Literal) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(int, int) = int
```

---

## Linha 232

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
4. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
5. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 233

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
5. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
6. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
7. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
8. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
9. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
10. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> int
11. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
12. Nó 'num' (Valor: 0.5): Regra 2.1 (Literal) -> real
13. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** real == int, e₂.valor > 0

---

## Linha 234

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
4. Nó 'id' (Valor: Y): Regra 2.2 (Identificador) -> int
5. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
6. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
7. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
8. Nó 'id' (Valor: Z): Regra 2.2 (Identificador) -> int
9. Nó 'id' (Valor: X): Regra 2.2 (Identificador) -> int
10. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int
11. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (int, int) -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : int
```
**Restrição:** int == int, int == int

---

## Linha 235

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
2. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, real) -> None
4. Nó 'id' (Valor: E): Regra 2.2 (Identificador) -> real
5. Nó 'id' (Valor: PI): Regra 2.2 (Identificador) -> real
6. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (real, real) -> None
7. Nó 'minus' (Valor: -): Regra 2.3 (Aritmética) com (None, None) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : None    Γ ⊢ e₂ : None
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ -) : promover_tipo(None, None) = None
```

---

## Linha 236

**Tipo Inferido Final:** `booleano`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
2. Nó 'id' (Valor: B): Regra 2.2 (Identificador) -> int
3. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
4. Nó 'id' (Valor: C): Regra 2.2 (Identificador) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
6. Nó 'id' (Valor: D): Regra 2.2 (Identificador) -> int
7. Nó 'id' (Valor: F): Regra 2.2 (Identificador) -> int
8. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (int, int) -> int
9. Nó 'id' (Valor: A): Regra 2.2 (Identificador) -> int
10. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (int, int) -> int
11. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.6: Operador Relacional**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ >) : booleano
```
**Restrição:** int, int ∈ {int, real}

---

## Linha 237

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
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

## Linha 238

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

## Linha 239

**Tipo Inferido Final:** `int`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
2. Nó 'id' (Valor: ERROSTESTE): Regra 2.2 (Identificador) -> None
3. Nó 'store': Regra 2.7 (Armazenamento) de 'int' em 'ERROSTESTE' -> int

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : int    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[ERROSTESTE ↦ {tipo: int}] ⊢ (e₁ ERROSTESTE) : int
```

---

## Linha 240

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'id' (Valor: MEMORIA_NAO_INICIALIZADA): Regra 2.2 (Identificador) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.2: Identificador**
```
Γ(MEMORIA_NAO_INICIALIZADA).tipo = None, Γ(MEMORIA_NAO_INICIALIZADA).inicializada = true
──────────────────────────────────────────────
Γ ⊢ MEMORIA_NAO_INICIALIZADA : None
```

---

## Linha 241

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.5): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
3. Nó 'div_int' (Valor: /): Regra 2.4 (Div/Mod) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ /) : None
```
**Restrição:** real == int, int == int

---

## Linha 242

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 3.5): Regra 2.1 (Literal) -> real
3. Nó 'mod' (Valor: %): Regra 2.4 (Div/Mod) com (int, real) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.4: Divisão/Módulo Inteiro**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : real
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ %) : None
```
**Restrição:** int == int, real == int

---

## Linha 243

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 2.5): Regra 2.1 (Literal) -> real
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

## Linha 244

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 245

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 2): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'pow' (Valor: ^): Regra 2.5 (Potência) com (int, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.5: Potenciação**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ ^) : None
```
**Restrição:** int == int, e₂.valor > 0

---

## Linha 246

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 3): Regra 2.1 (Literal) -> int
5. Nó 'plus' (Valor: +): Regra 2.3 (Aritmética) com (booleano, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ +) : promover_tipo(booleano, int) = None
```

---

## Linha 247

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
6. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
7. Nó 'mult' (Valor: *): Regra 2.3 (Aritmética) com (booleano, booleano) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : booleano    Γ ⊢ e₂ : booleano
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ *) : promover_tipo(booleano, booleano) = None
```

---

## Linha 248

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'gt' (Valor: >): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'id' (Valor: FLAG): Regra 2.2 (Identificador) -> None
5. Nó 'store': Regra 2.7 (Armazenamento) de 'booleano' em 'FLAG' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.7: Armazenamento**
```
Γ ⊢ e₁ : booleano    T ∈ {int, real}
──────────────────────────────────────────────────
Γ[FLAG ↦ {tipo: booleano}] ⊢ (e₁ FLAG) : None
```

---

## Linha 249

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

## Linha 250

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
3. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> ERRO
4. Nó 'while' (Valor: while): Regra 2.10 (Laço) com (cond:int, body:int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.10: Laço de Repetição**
```
Γ ⊢ e₁ : int    Γ ⊢ e₂ : int
─────────────────────────────────────
Γ ⊢ (e₁ e₂ while) : None
```
**Restrição:** int == booleano

---

## Linha 251

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10): Regra 2.1 (Literal) -> int
2. Nó 'num' (Valor: 5): Regra 2.1 (Literal) -> int
3. Nó 'lt' (Valor: <): Regra 2.6 (Relacional) com (int, int) -> booleano
4. Nó 'num' (Valor: 1): Regra 2.1 (Literal) -> int
5. Nó 'num' (Valor: 2.0): Regra 2.1 (Literal) -> real
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

## Linha 252

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

## Linha 253

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

## Linha 254

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: -1): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = -1

---

## Linha 255

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 999): Regra 2.1 (Literal) -> int
2. Nó 'res' (Valor: RES): Regra 2.8 (Histórico) com N='int' -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.8: Histórico**
```
Γ ⊢ e₁ : int    e₁.valor ≥ 1    historico[...].tipo = T
────────────────────────────────────────────────────────
Γ ⊢ (e₁ RES) : None
```
Contexto: N = 999

---

## Linha 256

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

## Linha 257

**Tipo Inferido Final:** `None`

### Processo de Inferência (Bottom-Up)

1. Nó 'num' (Valor: 10.0): Regra 2.1 (Literal) -> real
2. Nó 'num' (Valor: 0): Regra 2.1 (Literal) -> int
3. Nó 'div_real' (Valor: |): Regra 2.3 (Aritmética) com (real, int) -> None

### Regra de Dedução Formal (Nó Raiz)

**Regra 2.3: Operação Aritmética (com promoção)**
```
Γ ⊢ e₁ : real    Γ ⊢ e₂ : int
────────────────────────────────────────────────
Γ ⊢ (e₁ e₂ |) : promover_tipo(real, int) = None
```

