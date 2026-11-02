from __future__ import annotations

import sys
from dataclasses import dataclass

from src.rafnc.lexer import token


@dataclass
class ClassDeclaration:
    name: str
    members: list[ValueDeclaration]
    methods: list[FunctionDeclaration]
    irname: str


@dataclass
class MemberDeclaration:
    name: str
    mutable: bool
    typ: Value
    real_idx: int


@dataclass
class ValueDeclaration:
    name: str
    mutable: bool
    typ: Value
    expr: Expression
    irname: str


@dataclass
class FunctionDeclaration:
    name: str
    label: str | None
    typ: Value
    args: dict[str, Value]
    body: list[Node]
    irname: str


@dataclass
class ValueAssignment:
    reference: ClassPath | VariableRef
    assigner: str
    typ: Value
    expr: Expression
    irname: str


@dataclass
class ReturnStatement:
    expr: Expression | None


@dataclass
class MacroDefinition:
    name: str
    params: list[tuple[str, str]]
    body: list[token.Token]


@dataclass
class MacroCall:
    name: str
    args: list[token.Token]


@dataclass
class InlineIR:
    template: str
    args: list[Expression]
    expansion_id: int


Node = (
    ClassDeclaration
    | ValueDeclaration
    | FunctionDeclaration
    | MacroDefinition
    | MacroCall
    | InlineIR
)


@dataclass
class BinaryExpression:
    left: Expression
    right: Expression
    op: str
    typ: Value


@dataclass
class UnaryExpression:
    expr: Expression
    sign: str
    typ: Value


@dataclass
class PrimaryExpression:
    value: Value
    typ: Value


Expression = BinaryExpression | UnaryExpression | PrimaryExpression


@dataclass
class Integer64:
    value: int

    def __eq__(self, other):
        if not isinstance(other, Integer64):
            return False
        return self.value == other.value


@dataclass
class Float64:
    value: int

    def __eq__(self, other):
        if not isinstance(other, Float64):
            return False
        return self.value == other.value


@dataclass
class String:
    value: str


@dataclass
class Void:
    pass


@dataclass
class Class:
    name: str
    irname: str


@dataclass
class VariableRef:
    name: str
    mutable: bool
    irname: str
    typ: Value


@dataclass
class ClassPath:
    name: str
    irname: str
    child: ClassPath | VariableRef


@dataclass
class FunctionCall:
    name: str
    irname: str
    typ: Value
    args: list[Expression]


Value = (
    Class | Integer64 | Float64 | String | Void | VariableRef | ClassPath | FunctionCall
)
