# Árvore Sintática Atribuída - .\teste1.txt

**Gerado pelo compilador RPN - Fase 3**

## Expressão 1

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 10.428676643235324
  └─ id = A
```

## Expressão 2

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 20.53
  └─ id = B
```

## Expressão 3

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = -5.345345
  └─ id = C
```

## Expressão 4

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 5

**Tipo inferido:** `booleano`

```
lte : booleano = <=
  ├─ id : real = A
  └─ num : int = 10
```

## Expressão 6

**Tipo inferido:** `None`

```
res = RES
  └─ id : real = B
```

## Expressão 7

**Tipo inferido:** `booleano`

```
gte : booleano = >=
  ├─ id : real = B
  └─ num : int = 20
```

## Expressão 8

**Tipo inferido:** `booleano`

```
eq : booleano = ==
  ├─ id : real = C
  └─ num : int = -5
```

## Expressão 9

**Tipo inferido:** `booleano`

```
neq : booleano = !=
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 10

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 11

**Tipo inferido:** `real`

```
minus : real = -
  ├─ id : real = B
  └─ id : real = A
```

## Expressão 12

**Tipo inferido:** `int`

```
mult : int = *
  ├─ num : int = 10
  └─ num : int = 3
```

## Expressão 13

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ num : int = 100
  └─ num : int = 7
```

## Expressão 14

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 100
  └─ num : real = 7.0
```

## Expressão 15

**Tipo inferido:** `int`

```
mod : int = %
  ├─ num : int = 10
  └─ num : int = 3
```

## Expressão 16

**Tipo inferido:** `int`

```
pow : int = ^
  ├─ num : int = 2
  └─ num : int = 8
```

## Expressão 17

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : real = A
    └─ id : real = B
  ├─ if : int = if
    ├─ lt : booleano = <
      ├─ id : real = C
      └─ num : int = 0
    ├─ num : int = 1
    └─ num : int = 0
  └─ num : int = -1
```

## Expressão 18

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = I
```

## Expressão 19

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ num : int = 5
  └─ store : int
    ├─ plus : int = +
      ├─ id : int = I
      └─ num : int = 1
    └─ id = I
```

## Expressão 20

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 2
```

## Expressão 21

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 22

**Tipo inferido:** `real`

```
mult : real = *
  ├─ plus : real = +
    ├─ id : real = A
    └─ id : real = B
  └─ minus : real = -
    ├─ id : real = C
    └─ num : int = 10
```

## Expressão 23

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ mult : real = *
    ├─ id : real = A
    └─ id : real = B
  └─ id : real = C
```

## Expressão 24

**Tipo inferido:** `None`

```
gt = >
  ├─ mod = %
    ├─ num : int = 100
    └─ id : real = A
  └─ plus : real = +
    ├─ id : real = B
    └─ id : real = C
```

## Expressão 25

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = A
  └─ mult : real = *
    ├─ id : real = B
    └─ pow : real = ^
      ├─ id : real = C
      └─ num : int = 2
```

## Expressão 26

**Tipo inferido:** `real`

```
minus : real = -
  ├─ mult : real = *
    ├─ id : real = A
    └─ id : real = B
  └─ mult : real = *
    ├─ id : real = C
    └─ id : real = B
```

## Expressão 27

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = X
```

## Expressão 28

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 200
  └─ id = Y
```

## Expressão 29

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = -50.5
  └─ id = Z
```

## Expressão 30

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ num : int = 20
  └─ store : int
    ├─ plus : int = +
      ├─ id : int = I
      └─ num : int = 2
    └─ id = I
```

## Expressão 31

**Tipo inferido:** `int`

```
id : int = I
```

## Expressão 32

**Tipo inferido:** `None`

```
if = if
  ├─ gt : booleano = >
    ├─ id : real = A
    └─ num : int = 0
  ├─ if = if
    ├─ gt : booleano = >
      ├─ id : real = B
      └─ num : int = 0
    ├─ mult : real = *
      ├─ id : real = A
      └─ id : real = B
    └─ num : int = 0
  └─ num : int = 0
```

## Expressão 33

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = RAIO
```

## Expressão 34

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = PI
```

## Expressão 35

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = LIMIT
```

## Expressão 36

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = VALORANTIGO
```

## Expressão 37

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = RESULTADO
```

## Expressão 38

**Tipo inferido:** `int`

```
plus : int = +
  ├─ div_int : int = /
    ├─ if : int = if
      ├─ gt : booleano = >
        ├─ mult : int = *
          ├─ mult : int = *
            ├─ id : int = RAIO
            └─ id : int = RAIO
          └─ id : int = PI
        └─ id : int = LIMIT
      ├─ store : int
        ├─ plus : int = +
          ├─ res : int = RES
            └─ num : int = 1
          └─ id : int = VALORANTIGO
        └─ id = RESULTADO
      └─ num : int = 0
    └─ num : int = 2
  └─ div_int : int = /
    ├─ if : int = if
      ├─ gt : booleano = >
        ├─ mult : int = *
          ├─ mult : int = *
            ├─ id : int = RAIO
            └─ id : int = RAIO
          └─ id : int = PI
        └─ id : int = LIMIT
      ├─ store : int
        ├─ plus : int = +
          ├─ res : int = RES
            └─ num : int = 1
          └─ id : int = VALORANTIGO
        └─ id = RESULTADO
      └─ num : int = 0
    └─ num : int = 2
```

## Expressão 39

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = D
```

## Expressão 40

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = E
```

## Expressão 41

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = F
```

## Expressão 42

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = G
```

## Expressão 43

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = H
```

## Expressão 44

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = J
```

## Expressão 45

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = K
```

## Expressão 46

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = L
```

## Expressão 47

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = M
```

## Expressão 48

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = N
```

## Expressão 49

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = O
```

## Expressão 50

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = P
```

## Expressão 51

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = Q
```

## Expressão 52

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = R
```

## Expressão 53

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = S
```

## Expressão 54

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = T
```

## Expressão 55

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = U
```

## Expressão 56

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ plus : real = +
    ├─ id : real = A
    └─ id : real = B
  └─ mult : real = *
    ├─ id : real = C
    └─ id : int = D
```

## Expressão 57

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ minus : real = -
    ├─ plus : real = +
      ├─ mult : real = *
        ├─ plus : real = +
          ├─ id : real = A
          └─ id : real = B
        └─ plus : real = +
          ├─ id : real = C
          └─ id : int = D
      └─ mult : int = *
        ├─ plus : int = +
          ├─ id : int = E
          └─ id : int = F
        └─ plus : int = +
          ├─ id : int = G
          └─ id : int = H
    └─ div_int : int = /
      ├─ plus : int = +
        ├─ id : int = I
        └─ id : int = J
      └─ plus : int = +
        ├─ id : int = K
        └─ id : int = L
  └─ plus : int = +
    ├─ pow : int = ^
      ├─ plus : int = +
        ├─ id : int = M
        └─ id : int = N
      └─ plus : int = +
        ├─ id : int = O
        └─ id : int = P
    └─ mod : int = %
      ├─ plus : int = +
        ├─ id : int = Q
        └─ id : int = R
      └─ plus : int = +
        ├─ id : int = S
        └─ id : int = T
```

## Expressão 58

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = ZERO
```

## Expressão 59

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = UM
```

## Expressão 60

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = DEZ
```

## Expressão 61

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = CEM
```

## Expressão 62

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = -1
  └─ id = NEGATIVO
```

## Expressão 63

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 0.5
  └─ id = MEIO
```

## Expressão 64

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1000
  └─ id = MIL
```

## Expressão 65

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 3.14159265359
  └─ id = PI
```

## Expressão 66

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : real = A
    └─ id : real = B
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 67

**Tipo inferido:** `int`

```
if : int = if
  ├─ gte : booleano = >=
    ├─ id : real = A
    └─ num : int = 10
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 68

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = J
```

## Expressão 69

**Tipo inferido:** `int`

```
plus : int = +
  ├─ num : int = 10
  └─ num : int = 20
```

## Expressão 70

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ num : int = 15
  └─ num : int = 3
```

## Expressão 71

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : real = 10.5
  └─ num : real = 2.5
```

## Expressão 72

**Tipo inferido:** `int`

```
mod : int = %
  ├─ num : int = 10
  └─ num : int = 3
```

## Expressão 73

**Tipo inferido:** `int`

```
pow : int = ^
  ├─ num : int = 2
  └─ num : int = 8
```

## Expressão 74

**Tipo inferido:** `int`

```
plus : int = +
  ├─ id : int = X
  └─ num : int = 10
```

## Expressão 75

**Tipo inferido:** `int`

```
mult : int = *
  ├─ id : int = Y
  └─ num : int = 5
```

## Expressão 76

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 77

**Tipo inferido:** `real`

```
minus : real = -
  ├─ id : real = C
  └─ id : int = D
```

## Expressão 78

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ id : int = E
  └─ id : int = F
```

## Expressão 79

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 80

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ id : int = X
  └─ id : int = Y
```

## Expressão 81

**Tipo inferido:** `booleano`

```
eq : booleano = ==
  ├─ id : int = M
  └─ id : int = N
```

## Expressão 82

**Tipo inferido:** `booleano`

```
neq : booleano = !=
  ├─ id : int = P
  └─ id : int = Q
```

## Expressão 83

**Tipo inferido:** `booleano`

```
lte : booleano = <=
  ├─ id : int = R
  └─ id : int = S
```

## Expressão 84

**Tipo inferido:** `booleano`

```
gte : booleano = >=
  ├─ id : int = T
  └─ id : int = U
```

## Expressão 85

**Tipo inferido:** `real`

```
mult : real = *
  ├─ plus : real = +
    ├─ id : real = A
    └─ id : real = B
  └─ id : real = C
```

## Expressão 86

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ minus : int = -
    ├─ id : int = D
    └─ id : int = E
  └─ id : int = F
```

## Expressão 87

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = G
    └─ id : int = H
  └─ id : int = I
```

## Expressão 88

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 42
  └─ id = X
```

## Expressão 89

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = Y
```

## Expressão 90

**Tipo inferido:** `real`

```
store : real
  ├─ plus : real = +
    ├─ id : real = A
    └─ id : real = B
  └─ id = Z
```

## Expressão 91

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = N
    └─ num : int = 0
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 92

**Tipo inferido:** `real`

```
if : real = if
  ├─ lt : booleano = <
    ├─ id : int = X
    └─ id : int = Y
  ├─ id : real = A
  └─ id : real = B
```

## Expressão 93

**Tipo inferido:** `real`

```
pow : real = ^
  ├─ plus : real = +
    ├─ num : real = 45.6866
    └─ num : real = 0.5
  └─ num : int = 1
```

## Expressão 94

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = VALOR
```

## Expressão 95

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = VALOR
    └─ num : int = 10
  ├─ id : int = VALOR
  └─ num : int = 0
```

## Expressão 96

**Tipo inferido:** `None`

```
div_int = /
  ├─ id : real = PI
  └─ num : int = 180
```

## Expressão 97

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = METROS
```

## Expressão 98

**Tipo inferido:** `real`

```
mult : real = *
  ├─ id : int = METROS
  └─ num : real = 3.28084
```

## Expressão 99

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = POLEGADAS
```

## Expressão 100

**Tipo inferido:** `real`

```
mult : real = *
  ├─ id : int = POLEGADAS
  └─ num : real = 2.54
```

## Expressão 101

**Tipo inferido:** `real`

```
plus : real = +
  ├─ plus : real = +
    ├─ id : real = A
    └─ id : real = B
  └─ plus : real = +
    ├─ id : real = C
    └─ id : int = D
```

## Expressão 102

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = W
```

## Expressão 103

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : int = *
    ├─ id : int = X
    └─ id : int = Y
  └─ mult : real = *
    ├─ id : real = Z
    └─ id : int = W
```

## Expressão 104

**Tipo inferido:** `int`

```
minus : int = -
  ├─ minus : int = -
    ├─ id : int = M
    └─ id : int = N
  └─ minus : int = -
    ├─ id : int = O
    └─ id : int = P
```

## Expressão 105

**Tipo inferido:** `int`

```
if : int = if
  ├─ lte : booleano = <=
    ├─ id : int = N
    └─ num : int = 1
  ├─ num : int = 1
  └─ id : int = N
```

## Expressão 106

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = N
    └─ num : int = 0
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 107

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = MIN
```

## Expressão 108

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = MAX
```

## Expressão 109

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ minus : int = -
    ├─ id : int = VALOR
    └─ id : int = MIN
  └─ minus : int = -
    ├─ id : int = MAX
    └─ id : int = MIN
```

## Expressão 110

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = MEDIA
```

## Expressão 111

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = DESVIO
```

## Expressão 112

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ minus : int = -
    ├─ id : int = VALOR
    └─ id : int = MEDIA
  └─ id : int = DESVIO
```

## Expressão 113

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = VALOR
    └─ num : int = 0
  ├─ num : int = 0
  └─ id : int = VALOR
```

## Expressão 114

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = VALOR
    └─ num : int = 100
  ├─ num : int = 100
  └─ id : int = VALOR
```

## Expressão 115

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A11
```

## Expressão 116

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = B11
```

## Expressão 117

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A12
```

## Expressão 118

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = B21
```

## Expressão 119

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A21
```

## Expressão 120

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = B12
```

## Expressão 121

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A22
```

## Expressão 122

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = B22
```

## Expressão 123

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = A11
    └─ id : int = B11
  └─ mult : int = *
    ├─ id : int = A12
    └─ id : int = B21
```

## Expressão 124

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = A21
    └─ id : int = B12
  └─ mult : int = *
    ├─ id : int = A22
    └─ id : int = B22
```

## Expressão 125

**Tipo inferido:** `real`

```
minus : real = -
  ├─ mult : real = *
    ├─ id : real = A
    └─ id : int = D
  └─ mult : real = *
    ├─ id : real = B
    └─ id : real = C
```

## Expressão 126

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = TOTAL
```

## Expressão 127

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = VALOR
    └─ num : int = 100
  └─ id : int = TOTAL
```

## Expressão 128

**Tipo inferido:** `None`

```
div_int = /
  ├─ plus : real = +
    ├─ id : int = VALOR
    └─ num : real = 0.5
  └─ num : int = 1
```

## Expressão 129

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = CELSIUS
```

## Expressão 130

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = CELSIUS
    └─ num : int = 9
  └─ num : int = 5
```

## Expressão 131

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = FAHRENHEIT
```

## Expressão 132

**Tipo inferido:** `int`

```
mult : int = *
  ├─ minus : int = -
    ├─ id : int = FAHRENHEIT
    └─ num : int = 32
  └─ num : int = 5
```

## Expressão 133

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = SOMA
```

## Expressão 134

**Tipo inferido:** `int`

```
store : int
  ├─ plus : int = +
    ├─ id : int = SOMA
    └─ id : int = VALOR
  └─ id = SOMA
```

## Expressão 135

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = PRODUTO
```

## Expressão 136

**Tipo inferido:** `int`

```
store : int
  ├─ mult : int = *
    ├─ id : int = PRODUTO
    └─ id : int = VALOR
  └─ id = PRODUTO
```

## Expressão 137

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = VALOR
    └─ id : int = MAX
  ├─ id : int = VALOR
  └─ id : int = MAX
```

## Expressão 138

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = VALOR
    └─ id : int = MIN
  ├─ id : int = VALOR
  └─ id : int = MIN
```

## Expressão 139

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = VALOR
    └─ num : int = 0
  ├─ minus : int = -
    ├─ num : int = 0
    └─ id : int = VALOR
  └─ id : int = VALOR
```

## Expressão 140

**Tipo inferido:** `None`

```
if = if
  ├─ mod : int = %
    ├─ id : int = X
    └─ num : int = 2
  ├─ num : int = 0
  └─ num : int = 1
```

## Expressão 141

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 100
  └─ id = X
```

## Expressão 142

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 50
  └─ id = Y
```

## Expressão 143

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 25
  └─ id = Z
```

## Expressão 144

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 3.14159
  └─ id = PI
```

## Expressão 145

**Tipo inferido:** `real`

```
store : real
  ├─ num : real = 2.71828
  └─ id = E
```

## Expressão 146

**Tipo inferido:** `int`

```
res : int = RES
  └─ num : int = 4
```

## Expressão 147

**Tipo inferido:** `int`

```
minus : int = -
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 148

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 149

**Tipo inferido:** `int`

```
plus : int = +
  ├─ pow : int = ^
    ├─ id : int = X
    └─ num : int = 2
  └─ pow : int = ^
    ├─ id : int = Y
    └─ num : int = 2
```

## Expressão 150

**Tipo inferido:** `real`

```
pow : real = ^
  ├─ mult : real = *
    ├─ id : real = PI
    └─ num : int = 2
  └─ num : int = 10
```

## Expressão 151

**Tipo inferido:** `real`

```
plus : real = +
  ├─ id : real = E
  └─ div_real : real = |
    ├─ id : int = X
    └─ id : int = Y
```

## Expressão 152

**Tipo inferido:** `None`

```
mult = *
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  └─ gt : booleano = >
    ├─ id : int = Z
    └─ num : int = 0
```

## Expressão 153

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 154

**Tipo inferido:** `booleano`

```
gte : booleano = >=
  ├─ plus : int = +
    ├─ id : int = X
    └─ plus : int = +
      ├─ id : int = Y
      └─ id : int = Z
  └─ num : int = 100
```

## Expressão 155

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : real = PI
    └─ id : real = E
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 156

**Tipo inferido:** `None`

```
mult = *
  ├─ lt : booleano = <
    ├─ id : int = X
    └─ id : int = Y
  └─ lt : booleano = <
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 157

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 158

**Tipo inferido:** `None`

```
eq = ==
  ├─ mod = %
    ├─ id : int = X
    └─ num : real = 1001.445452112
  └─ num : int = 0
```

## Expressão 159

**Tipo inferido:** `booleano`

```
eq : booleano = ==
  ├─ mod : int = %
    ├─ id : int = Z
    └─ num : int = 5
  └─ num : int = 2
```

## Expressão 160

**Tipo inferido:** `int`

```
plus : int = +
  ├─ pow : int = ^
    ├─ num : int = 2
    └─ id : int = X
  └─ pow : int = ^
    ├─ num : int = 3
    └─ id : int = Y
```

## Expressão 161

**Tipo inferido:** `int`

```
mod : int = %
  ├─ pow : int = ^
    ├─ id : int = X
    └─ id : int = Y
  └─ id : int = Z
```

## Expressão 162

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ id : int = X
    └─ num : real = 3.7557
  └─ div_real : real = |
    ├─ id : int = Y
    └─ num : real = 2.3345
```

## Expressão 163

**Tipo inferido:** `real`

```
minus : real = -
  ├─ div_int : int = /
    ├─ id : int = Z
    └─ num : int = 4
  └─ div_real : real = |
    ├─ id : int = X
    └─ num : int = 5
```

## Expressão 164

**Tipo inferido:** `real`

```
mult : real = *
  ├─ div_real : real = |
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ id : int = Z
  └─ num : int = 2
```

## Expressão 165

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ num : real = 100.54
    └─ num : int = 7
  └─ div_real : real = |
    ├─ num : int = 3
    └─ num : int = 2
```

## Expressão 166

**Tipo inferido:** `real`

```
minus : real = -
  ├─ div_real : real = |
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Z
    └─ num : int = 2
```

## Expressão 167

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ num : int = 50
  ├─ minus : int = -
    ├─ id : int = X
    └─ num : int = 10
  └─ plus : int = +
    ├─ id : int = X
    └─ num : int = 10
```

## Expressão 168

**Tipo inferido:** `int`

```
if : int = if
  ├─ eq : booleano = ==
    ├─ id : int = Y
    └─ id : int = Z
  ├─ num : int = 1
  └─ num : int = -1
```

## Expressão 169

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  ├─ id : int = X
  └─ id : int = Y
```

## Expressão 170

**Tipo inferido:** `int`

```
if : int = if
  ├─ neq : booleano = !=
    ├─ id : int = Z
    └─ num : int = 0
  ├─ div_int : int = /
    ├─ id : int = X
    └─ id : int = Z
  └─ num : int = 0
```

## Expressão 171

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ plus : int = +
      ├─ id : int = X
      └─ id : int = Y
    └─ num : int = 100
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 172

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = I
```

## Expressão 173

**Tipo inferido:** `int`

```
while : int = while
  ├─ lt : booleano = <
    ├─ id : int = I
    └─ num : int = 10
  └─ store : int
    ├─ plus : int = +
      ├─ id : int = I
      └─ num : int = 1
    └─ id = I
```

## Expressão 174

**Tipo inferido:** `int`

```
id : int = I
```

## Expressão 175

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = CONTADOR
```

## Expressão 176

**Tipo inferido:** `int`

```
while : int = while
  ├─ lte : booleano = <=
    ├─ id : int = CONTADOR
    └─ num : int = 5
  └─ store : int
    ├─ mult : int = *
      ├─ id : int = CONTADOR
      └─ num : int = 2
    └─ id = CONTADOR
```

## Expressão 177

**Tipo inferido:** `int`

```
id : int = CONTADOR
```

## Expressão 178

**Tipo inferido:** `int`

```
minus : int = -
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ num : int = 10
      └─ num : int = 20
    └─ num : int = 5
  └─ num : int = 2
```

## Expressão 179

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ num : int = 2
```

## Expressão 180

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ id : real = PI
    └─ num : int = 2
  └─ id : int = X
```

## Expressão 181

**Tipo inferido:** `real`

```
plus : real = +
  ├─ pow : real = ^
    ├─ id : real = E
    └─ id : int = X
  └─ num : int = 1
```

## Expressão 182

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ mult : int = *
    ├─ id : int = X
    └─ id : int = Y
  └─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
```

## Expressão 183

**Tipo inferido:** `None`

```
pow = ^
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ id : int = X
      └─ num : int = 2
    └─ pow : int = ^
      ├─ id : int = Y
      └─ num : int = 2
  └─ num : real = 0.5
```

## Expressão 184

**Tipo inferido:** `None`

```
mult = *
  ├─ gt : booleano = >
    ├─ id : int = X
    └─ id : int = Y
  └─ gt : booleano = >
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 185

**Tipo inferido:** `None`

```
mult = *
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ num : int = 0
    └─ gt : booleano = >
      ├─ id : int = Y
      └─ num : int = 0
  └─ gt : booleano = >
    ├─ id : int = Z
    └─ num : int = 0
```

## Expressão 186

**Tipo inferido:** `None`

```
mult = *
  ├─ gte : booleano = >=
    ├─ id : int = X
    └─ id : int = Y
  └─ lte : booleano = <=
    ├─ id : int = X
    └─ id : int = Z
```

## Expressão 187

**Tipo inferido:** `None`

```
mult = *
  ├─ neq : booleano = !=
    ├─ id : int = X
    └─ id : int = Y
  └─ neq : booleano = !=
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 188

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ id : int = X
    └─ id : int = Y
  └─ minus : int = -
    ├─ id : int = Z
    └─ num : int = 10
```

## Expressão 189

**Tipo inferido:** `int`

```
minus : int = -
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ id : int = X
      └─ num : int = 2
    └─ pow : int = ^
      ├─ id : int = Y
      └─ num : int = 2
  └─ pow : int = ^
    ├─ id : int = Z
    └─ num : int = 2
```

## Expressão 190

**Tipo inferido:** `None`

```
plus = +
  ├─ div_int = /
    ├─ mult : real = *
      ├─ id : real = PI
      └─ id : int = X
    └─ num : int = 2
  └─ div_int = /
    ├─ mult : real = *
      ├─ id : real = E
      └─ id : int = Y
    └─ num : int = 3
```

## Expressão 191

**Tipo inferido:** `int`

```
mult : int = *
  ├─ div_int : int = /
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 192

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ num : int = 100
  └─ mod : int = %
    ├─ id : int = Y
    └─ num : int = 100
```

## Expressão 193

**Tipo inferido:** `None`

```
plus = +
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ id : int = Y
    └─ num : int = 1
  └─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = Z
      └─ id : int = Y
    └─ num : int = 1
```

## Expressão 194

**Tipo inferido:** `None`

```
eq = ==
  ├─ mult = *
    ├─ gt : booleano = >
      ├─ id : int = X
      └─ num : int = 0
    └─ gt : booleano = >
      ├─ id : int = Y
      └─ num : int = 0
  └─ num : int = 1
```

## Expressão 195

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = A
```

## Expressão 196

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 2
  └─ id = B
```

## Expressão 197

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 3
  └─ id = C
```

## Expressão 198

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 4
  └─ id = D
```

## Expressão 199

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 5
  └─ id = F
```

## Expressão 200

**Tipo inferido:** `int`

```
plus : int = +
  ├─ plus : int = +
    ├─ plus : int = +
      ├─ plus : int = +
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 201

**Tipo inferido:** `int`

```
mult : int = *
  ├─ mult : int = *
    ├─ mult : int = *
      ├─ mult : int = *
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 202

**Tipo inferido:** `int`

```
minus : int = -
  ├─ minus : int = -
    ├─ minus : int = -
      ├─ minus : int = -
        ├─ id : int = F
        └─ id : int = D
      └─ id : int = C
    └─ id : int = B
  └─ id : int = A
```

## Expressão 203

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ div_int : int = /
    ├─ div_int : int = /
      ├─ div_int : int = /
        ├─ id : int = A
        └─ id : int = B
      └─ id : int = C
    └─ id : int = D
  └─ id : int = F
```

## Expressão 204

**Tipo inferido:** `int`

```
if : int = if
  ├─ lt : booleano = <
    ├─ id : int = A
    └─ id : int = B
  ├─ if : int = if
    ├─ lt : booleano = <
      ├─ id : int = C
      └─ id : int = D
    ├─ num : int = 1
    └─ num : int = 2
  └─ num : int = 3
```

## Expressão 205

**Tipo inferido:** `int`

```
if : int = if
  ├─ gt : booleano = >
    ├─ id : int = A
    └─ num : int = 0
  ├─ if : int = if
    ├─ gt : booleano = >
      ├─ id : int = B
      └─ num : int = 0
    ├─ plus : int = +
      ├─ id : int = A
      └─ id : int = B
    └─ minus : int = -
      ├─ id : int = A
      └─ id : int = B
  └─ num : int = 0
```

## Expressão 206

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 1
  └─ num : int = 3
```

## Expressão 207

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 2
  └─ num : int = 3
```

## Expressão 208

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 5
  └─ num : int = 6
```

## Expressão 209

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 22
  └─ num : int = 7
```

## Expressão 210

**Tipo inferido:** `real`

```
div_real : real = |
  ├─ num : int = 355
  └─ num : int = 113
```

## Expressão 211

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ id : int = X
```

## Expressão 212

**Tipo inferido:** `int`

```
minus : int = -
  ├─ num : int = 0
  └─ plus : int = +
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 213

**Tipo inferido:** `booleano`

```
lt : booleano = <
  ├─ minus : int = -
    ├─ id : int = A
    └─ id : int = B
  └─ num : int = 0
```

## Expressão 214

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 215

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ id : int = A
    └─ id : int = B
  └─ id : int = C
```

## Expressão 216

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mult : int = *
    ├─ plus : int = +
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ id : int = D
```

## Expressão 217

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ id : int = D
```

## Expressão 218

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 10
  └─ id = N
```

## Expressão 219

**Tipo inferido:** `int`

```
while : int = while
  ├─ gt : booleano = >
    ├─ id : int = N
    └─ num : int = 0
  └─ store : int
    ├─ minus : int = -
      ├─ id : int = N
      └─ num : int = 1
    └─ id = N
```

## Expressão 220

**Tipo inferido:** `int`

```
id : int = N
```

## Expressão 221

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = SOMA
```

## Expressão 222

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 1
  └─ id = I
```

## Expressão 223

**Tipo inferido:** `int`

```
while : int = while
  ├─ lte : booleano = <=
    ├─ id : int = I
    └─ num : int = 10
  └─ mult : int = *
    ├─ store : int
      ├─ plus : int = +
        ├─ id : int = SOMA
        └─ id : int = I
      └─ id = SOMA
    └─ store : int
      ├─ plus : int = +
        ├─ id : int = I
        └─ num : int = 1
      └─ id = I
```

## Expressão 224

**Tipo inferido:** `int`

```
id : int = SOMA
```

## Expressão 225

**Tipo inferido:** `int`

```
minus : int = -
  ├─ mult : int = *
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ id : int = Y
  └─ id : int = X
```

## Expressão 226

**Tipo inferido:** `int`

```
plus : int = +
  ├─ mod : int = %
    ├─ id : int = X
    └─ id : int = Y
  └─ div_int : int = /
    ├─ id : int = Y
    └─ num : int = 2
```

## Expressão 227

**Tipo inferido:** `int`

```
plus : int = +
  ├─ div_int : int = /
    ├─ num : int = 100
    └─ num : int = 7
  └─ mod : int = %
    ├─ num : int = 100
    └─ num : int = 7
```

## Expressão 228

**Tipo inferido:** `real`

```
mult : real = *
  ├─ id : real = PI
  └─ pow : int = ^
    ├─ num : int = 5
    └─ num : int = 2
```

## Expressão 229

**Tipo inferido:** `real`

```
mult : real = *
  ├─ mult : real = *
    ├─ num : int = 2
    └─ id : real = PI
  └─ num : int = 5
```

## Expressão 230

**Tipo inferido:** `int`

```
mult : int = *
  ├─ mult : int = *
    ├─ num : int = 10
    └─ num : int = 20
  └─ num : int = 2
```

## Expressão 231

**Tipo inferido:** `int`

```
mult : int = *
  ├─ plus : int = +
    ├─ num : int = 10
    └─ num : int = 20
  └─ num : int = 2
```

## Expressão 232

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ id : int = X
  └─ plus : int = +
    ├─ id : int = Y
    └─ id : int = Z
```

## Expressão 233

**Tipo inferido:** `None`

```
pow = ^
  ├─ plus : int = +
    ├─ pow : int = ^
      ├─ plus : int = +
        ├─ id : int = A
        └─ id : int = B
      └─ num : int = 2
    └─ pow : int = ^
      ├─ plus : int = +
        ├─ id : int = C
        └─ id : int = D
      └─ num : int = 2
  └─ num : real = 0.5
```

## Expressão 234

**Tipo inferido:** `int`

```
div_int : int = /
  ├─ div_int : int = /
    ├─ div_int : int = /
      ├─ id : int = X
      └─ id : int = Y
    └─ div_int : int = /
      ├─ id : int = Y
      └─ id : int = Z
  └─ div_int : int = /
    ├─ id : int = Z
    └─ id : int = X
```

## Expressão 235

**Tipo inferido:** `None`

```
minus = -
  ├─ pow = ^
    ├─ id : real = PI
    └─ id : real = E
  └─ pow = ^
    ├─ id : real = E
    └─ id : real = PI
```

## Expressão 236

**Tipo inferido:** `booleano`

```
gt : booleano = >
  ├─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = A
      └─ id : int = B
    └─ id : int = C
  └─ plus : int = +
    ├─ mult : int = *
      ├─ id : int = D
      └─ id : int = F
    └─ id : int = A
```

## Expressão 237

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = A
```

## Expressão 238

**Tipo inferido:** `None`

```
res = RES
  └─ id : int = A
```

## Expressão 239

**Tipo inferido:** `int`

```
store : int
  ├─ num : int = 0
  └─ id = ERROSTESTE
```

## Expressão 240

**Tipo inferido:** `None`

```
id = MEMORIA_NAO_INICIALIZADA
```

## Expressão 241

**Tipo inferido:** `None`

```
div_int = /
  ├─ num : real = 10.5
  └─ num : int = 3
```

## Expressão 242

**Tipo inferido:** `None`

```
mod = %
  ├─ num : int = 10
  └─ num : real = 3.5
```

## Expressão 243

**Tipo inferido:** `None`

```
pow = ^
  ├─ num : int = 2
  └─ num : real = 2.5
```

## Expressão 244

**Tipo inferido:** `None`

```
pow = ^
  ├─ num : int = 2
  └─ num : int = -1
```

## Expressão 245

**Tipo inferido:** `None`

```
pow = ^
  ├─ num : int = 2
  └─ num : int = 0
```

## Expressão 246

**Tipo inferido:** `None`

```
plus = +
  ├─ lt : booleano = <
    ├─ num : int = 10
    └─ num : int = 5
  └─ num : int = 3
```

## Expressão 247

**Tipo inferido:** `None`

```
mult = *
  ├─ gt : booleano = >
    ├─ num : int = 10
    └─ num : int = 5
  └─ lt : booleano = <
    ├─ num : int = 5
    └─ num : int = 1
```

## Expressão 248

**Tipo inferido:** `None`

```
store
  ├─ gt : booleano = >
    ├─ num : int = 10
    └─ num : int = 5
  └─ id = FLAG
```

## Expressão 249

**Tipo inferido:** `None`

```
if = if
  ├─ num : int = 10
  ├─ num : int = 1
  └─ num : int = 0
```

## Expressão 250

**Tipo inferido:** `None`

```
while = while
  ├─ num : int = 5
  ├─ num : int = 1
  └─ num = 0
```

## Expressão 251

**Tipo inferido:** `None`

```
if = if
  ├─ lt : booleano = <
    ├─ num : int = 10
    └─ num : int = 5
  ├─ num : int = 1
  └─ num : real = 2.0
```

## Expressão 252

**Tipo inferido:** `None`

```
res = RES
  └─ num : real = 1.5
```

## Expressão 253

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = 0
```

## Expressão 254

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = -1
```

## Expressão 255

**Tipo inferido:** `None`

```
res = RES
  └─ num : int = 999
```

## Expressão 256

**Tipo inferido:** `None`

```
div_int = /
  ├─ num : int = 10
  └─ num : int = 0
```

## Expressão 257

**Tipo inferido:** `None`

```
div_real = |
  ├─ num : real = 10.0
  └─ num : int = 0
```

