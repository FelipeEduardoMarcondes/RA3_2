# Árvore Sintática Atribuída - .\teste3.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = A
```

## Expressão 2

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 5.5
  └─ id = B
```

## Expressão 3

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : int = A
  └─ id : real = B
```

## Expressão 4

**Tipo inferido:** `None`

```
id = VAR_NAO_EXISTENTE
```

## Expressão 5

**Tipo inferido:** `None`

```
div_int = /
  ├─ num : int = 10
  └─ num : real = 3.0
```

## Expressão 6

**Tipo inferido:** `None`

```
mod = %
  ├─ num : real = 10.0
  └─ num : int = 3
```

## Expressão 7

**Tipo inferido:** `None`

```
pow = ^
  ├─ id : int = A
  └─ num : real = 1.5
```

## Expressão 8

**Tipo inferido:** `None`

```
pow = ^
  ├─ id : real = B
  └─ num : int = -2
```

## Expressão 9

**Tipo inferido:** `None`

```
pow = ^
  ├─ id : real = B
  └─ num : int = 0
```

## Expressão 10

**Tipo inferido:** `None`

```
plus = +
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ id : real = B
  └─ num : int = 10
```

## Expressão 11

**Tipo inferido:** `None`

```
mult = *
  ├─ eq : booleano = ==
    ├─ id : int = A
    └─ num : int = 5
  └─ gt : booleano = >
    ├─ id : real = B
    └─ num : int = 2
```

## Expressão 12

**Tipo inferido:** `None`

```
store
  ├─ id = RESULTADO_BOOL
  └─ id = FLAG
```

## Expressão 13

**Tipo inferido:** `None`

```
div_int = /
  ├─ id = FLAG
  └─ num : int = 10
```

## Expressão 14

**Tipo inferido:** `None`

```
if = if
  ├─ num : int = 10
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 15

**Tipo inferido:** `None`

```
if = if
  ├─ id : int = A
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 16

**Tipo inferido:** `None`

```
while = while
  ├─ id : real = B
  ├─ num : int = 1
  └─ num = 0
```

## Expressão 17

**Tipo inferido:** `None`

```
if = if
  ├─ eq : booleano = ==
    ├─ id : int = A
    └─ num : int = 10
  ├─ num : int = 1
  └─ num : real = 1.5
```

## Expressão 18

**Tipo inferido:** `None`

```
if = if
  ├─ eq : booleano = ==
    ├─ id : real = B
    └─ num : real = 5.5
  ├─ id : int = A
  └─ id : real = B
```

## Expressão 19

**Tipo inferido:** `None`

```
if = if
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ num : int = 10
  ├─ if = if
    ├─ gt : booleano = >
      ├─ id : real = B
      └─ num : int = 1
    ├─ num : int = 1
    └─ num : real = 2.0
  └─ num : int = 0
```

## Expressão 20

**Tipo inferido:** `None`

```
res = RES
  └─ num : real = 1.5
```

## Expressão 21

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = 0
```

## Expressão 22

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = -10
```

## Expressão 23

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = 99999
```

## Expressão 24

**Tipo inferido:** `None`

```
res = RES
  └─ id : int = A
```

## Expressão 25

**Tipo inferido:** `None`

```
div_int = /
  ├─ num : int = 10
  └─ num : int = 0
```

## Expressão 26

**Tipo inferido:** `None`

```
div_real = |
  ├─ id : real = B
  └─ num : real = 0.0
```

## Expressão 27

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = ZER
```

## Expressão 28

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ id : int = A
  └─ id : int = ZER
```

## Expressão 29

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ id : real = B
  └─ id : int = ZER
```

## Expressão 30

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = ZER
    └─ num : int = 0
  ├─ num : int = 1
  └─ div_int : int = /
    ├─ num : int = 100
    └─ id : int = ZER
```

## Expressão 31

**Tipo inferido:** `real`

```
if : real = if
  ├─ eq : booleano = ==
    ├─ id : int = ZER
    └─ num : int = 0
  ├─ num : real = 1.0
  └─ div_real : real = |
    ├─ num : real = 100.0
    └─ id : int = ZER
```

## Expressão 32

**Tipo inferido:** `int`

```
num : int = 1
```

## Expressão 33

**Tipo inferido:** `int`

```
num : int = 2
```

## Expressão 34

**Tipo inferido:** `int`

```
num : int = 3
```

## Expressão 35

**Tipo inferido:** `int`

```
num : int = 4
```

## Expressão 36

**Tipo inferido:** `int`

```
num : int = 5
```

## Expressão 37

**Tipo inferido:** `int`

```
num : int = 6
```

## Expressão 38

**Tipo inferido:** `int`

```
plus : int = +
  ├─ plus : int = +
    ├─ res : int = RES
      └─ num : int = 1
    └─ res : int = RES
      └─ num : int = 3
  └─ res : int = RES
    └─ num : int = 5
```

## Expressão 39

**Tipo inferido:** `real`

```
plus : real = +
  ├─ plus : real = +
    ├─ res : int = RES
      └─ num : int = 1
    └─ mult : real = *
      ├─ id : real = B
      └─ num : real = 2.0
  └─ id : int = A
```

