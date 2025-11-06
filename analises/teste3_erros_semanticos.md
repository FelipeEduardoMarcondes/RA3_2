# Relatório de Erros Semânticos

 **23 erro(s) encontrado(s):**

1. AVISO SEMÂNTICO [Linha 24]: RES usado com variável (A). Tipo não pode ser verificado estaticamente.
Contexto: (A RES)

2. ERRO SEMÂNTICO [Linha 10]: Operador aritmético não aceita operandos booleanos
Contexto: (booleano int plus)

3. ERRO SEMÂNTICO [Linha 11]: Operador aritmético não aceita operandos booleanos
Contexto: (booleano booleano mult)

4. ERRO SEMÂNTICO [Linha 12]: Memória 'RESULTADO_BOOL' utilizada sem inicialização
Contexto: (RESULTADO_BOOL)

5. ERRO SEMÂNTICO [Linha 13]: Memória 'FLAG' utilizada sem inicialização
Contexto: (FLAG)

6. ERRO SEMÂNTICO [Linha 14]: Condição de IF deve ser booleana, encontrado 'int'
Contexto: (... ... ... if)

7. ERRO SEMÂNTICO [Linha 15]: Condição de IF deve ser booleana, encontrado 'int'
Contexto: (... ... ... if)

8. ERRO SEMÂNTICO [Linha 16]: Condição de WHILE deve ser booleana, encontrado 'real'
Contexto: (... ... while)

9. ERRO SEMÂNTICO [Linha 17]: Ramos de IF devem ter mesmo tipo: 'int' vs 'real'
Contexto: (... ... ... if)

10. ERRO SEMÂNTICO [Linha 18]: Ramos de IF devem ter mesmo tipo: 'int' vs 'real'
Contexto: (... ... ... if)

11. ERRO SEMÂNTICO [Linha 19]: Ramos de IF devem ter mesmo tipo: 'int' vs 'real'
Contexto: (... ... ... if)

12. ERRO SEMÂNTICO [Linha 20]: Argumento de RES deve ser inteiro, encontrado 'real'
Contexto: (1.5 RES)

13. ERRO SEMÂNTICO [Linha 21]: RES requer valor positivo (>= 1), encontrado 0
Contexto: (0 RES)

14. ERRO SEMÂNTICO [Linha 22]: RES requer valor positivo (>= 1), encontrado -10
Contexto: (-10 RES)

15. ERRO SEMÂNTICO [Linha 23]: RES(99999) referencia linha inexistente
Só existem 22 expressões anteriores
Contexto: (99999 RES)

16. ERRO SEMÂNTICO [Linha 25]: Divisão por zero com operador '/'
Contexto: (... 0 /)

17. ERRO SEMÂNTICO [Linha 26]: Divisão por zero com operador '|'
Contexto: (... 0 |)

18. ERRO SEMÂNTICO [Linha 4]: Memória 'VAR_NAO_EXISTENTE' utilizada sem inicialização
Contexto: (VAR_NAO_EXISTENTE)

19. ERRO SEMÂNTICO [Linha 5]: Operador '/' requer operandos inteiros, encontrado 'int' e 'real'
Contexto: (... ... /)

20. ERRO SEMÂNTICO [Linha 6]: Operador '%' requer operandos inteiros, encontrado 'real' e 'int'
Contexto: (... ... %)

21. ERRO SEMÂNTICO [Linha 7]: Expoente de potenciação deve ser inteiro, encontrado 'real'
Contexto: (... ... ^)

22. ERRO SEMÂNTICO [Linha 8]: Expoente de potenciação deve ser positivo (>= 1), encontrado -2
Contexto: (... -2 ^)

23. ERRO SEMÂNTICO [Linha 9]: Expoente de potenciação deve ser positivo (>= 1), encontrado 0
Contexto: (... 0 ^)

