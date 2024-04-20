# TPC6: GIC LL(1)

## 2024-04-13

## Autor:
- A100538
- Ivan Sérgio Rocha Ribeiro

## Resumo:

Foi desenvolvida uma Gramática Independente de Contexto para uma linguagem descrita nos exemplos mostrados a seguir, e respeitando a prioridade dos operadores. A gramática deve obedecer a condicao LL(1).

- ?a
- b = a * 2 / (27-3)
- ! a + b
- c = a * b / (a / b)

# Resolucao

T = {`?`, `VAR`, `NUM`, `=`, `*`, `/`, `(`, `)`, `-`, `!`, `+`}

N = {`S`,`Var`, `Num`, `Exp`, `ExpAux`, `Termo`, `TermoAux`, `Fator`}

```python
p = {
	p1:    S : '?' Exp
    p2:      | '!' Exp
    p3:      | Var '=' Exp

	p4:    Exp : Termo ExpAux

    p5:    ExpAux : '+' Exp
    p6:           | '-' Exp
    p7:           | &

    p8:    Termo : Fator TermoAux

    p9:    Fator : '(' Exp ')'
    p10:         | Num
    p11:         | Var

    p12:   TermoAux : '*' Termo
    p13:            | '/' Termo
    p14:            | &

	p15:   Var : VAR
	p16:   Num : NUM
}
```

# Lookaheads

LA(p1) = {`?`}

LA(p2) = {`!`}

LA(p3) = FirstN(Var) = {`VAR`}

LA(p4) = FirstN(Termo) = FirstN(Fator) = {`(`, `NUM`, `VAR`}

LA(p5) = {`+`}

LA(p6) = {`-`}

LA(p7) = Follow(ExpAux) = ??

LA(p8) = Follow(Fator) = ??

LA(p9) = {`(`}

LA(p10) = FirstN(Num) = {`NUM`}

LA(p11) = FirstN(Var) = {`VAR`}

LA(p12) = {`*`}

LA(p13) = {`/`}

LA(p14) = Follow(TermoAux) = ??

LA(p15) = {`VAR`}

LA(p16) = {`NUM`}

## Interseção

LA(p1) ∩ LA(p2) ∩ LA(p3) = {`?`} ∩ {`!`} ∩ {`VAR`} = ∅

LA(p5) ∩ LA(p6) ∩ LA(p7) = {`+`} ∩ {`-`} ∩ {??} = ∅

LA(p9) ∩ LA(p10) ∩ LA(p11) = {`(`} ∩ {`VAR`} ∩ {`NUM`} = ∅

LA(p12) ∩ LA(p13) ∩ LA(p14) = {`*`} ∩ {`/`} ∩ {??} = ∅

LA(p15) ∩ LA(p16) = {`VAR`} ∩ {`NUM`} = ∅
