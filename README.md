# ABSI

ABSTRACT SIGNAL PROGRAMMING LANGUAGE

## Introduction

ABSI is a programming language whose all keywords are symbols.

## Types

## Operators

### Traditional Operators

| Symbol | Description | Example |
| ------ | ----------- | ------- |
| `+`    | Addition    | `1 + 2` |
| `-`    | Subtraction | `1 - 2` |
| `*`    | Multiplication | `1 * 2` |
| `/`    | Division    | `1 / 2` |
| `^`    | Exponentiation | `1 ^ 2` |
| `=`    | Assignment  | `a = 1` |
| `==`   | Equality    | `x == y` |
| `!=`   | Inequality  | `1 != 2` |
| `>`    | Greater than | `1 > 2` |
| `<`    | Less than   | `1 < 2` |
| `>=`   | Greater than or equal to | `1 >= 2` |
| `<=`   | Less than or equal to | `1 <= 2` |
| `!`    | Not         | `!1` |
| `&`    | And         | `(x>0) & (y>0)` |
| `\|`   | Or          | `(x<0) \| (x>1)` |
| `~~`   | Bitwise NOT | `~~1` |
| `&&`   | Bitwise AND | `1 && 2` |
| `\|\|` | Bitwise OR  | `1 \|\| 2` |
| `^^`   | Bitwise XOR | `1 ^^ 2` |

### Control Flow

| Symbol        | Description |
| ------------- | ----------- |
| `()?{}!{}`    | If-Else     |
| `(x:xs){}`    | For         |
| `(flag:?){}`  | While       |
| `->\|`        | Break       |
| `->>`         | Continue    |

### Functions

```absi
(TypeR r1, TypeR r2, TypeP p0) foo(TypeA a0, TypeB b1, TypeC c2, TypeD d0=0) = {
    # function body
    >>> r1, r2, p0;
}

p = foo(a, b, c, d).p0;
```

Types, return values and parameters are optional.

Example:

```absi
a_in_list1(a0, as) = {
    (a:as){
        (a == a0) ? {
            >>> +;  # currently use _+
        }
    }
    >>> -;  # currently use _-
}

>>> types >> Bool, Int, List;

Bool a_in_list2(Int a0, List as) = {
    i = 0;
    (as[i]:?){
        (as[i] == a0) ? {
            >>> +;
        }
        i += 1;
    }
    >>> -;
}

# same as a0<-as
```

### Classes

```absi
Foo(TypeA a, TypeB b, TypeC c) = _{
    .a = a;
    .b = b;
    .c = c;
    .getA() = {
        >>> .a;
    }
}

EFoo(..., TypeD d) = Foo(...){
    .d = d;
    .getD() = {
        >>> .d;
    }
}

FFoo(TypeE e) = EFoo(0, 0, 0, d0){
    .e = e;
    .getE() = {
        >>> .e;
    }
}
```

## Compare with Python

### Python Keywords

| ABSI      | Python     |
| --------- | ---------- |
| `+`       | `True`     |
| `-`       | `False`    |
| `*`       | `None`     |
| `&`       | `and`      |
|           | `as`       |
| `()?!!!`  | `assert`   |
| `->\|`    | `break`    |
| `=_{}`    | `class`    |
| `->>`     | `continue` |
| `_()={}`  | `def`      |
| `!_!`     | `del`      |
|           | `elif`     |
| `!{}`     | `else`     |
| `!{}`     | `except`   |
|           | `finally`  |
| `(:){}`   | `for`      |
| `>>>`     | `from`     |
| `{_}`, `{{_}}`, ...  | `global` |
| `?`       | `if`       |
| `>>`      | `import`   |
| `<-`      | `in`       |
| `===`     | `is`       |
| `*()={}`  | `lambda`   |
| `{_}`     | `nonlocal` |
| `!`       | `not`      |
| `\|`      | `or`       |
| `...`     | `pass`     |
| `!!!`     | `raise`    |
| `>>>`     | `return`   |
| `{}->?`   | `try`      |
| `(:?)`    | `while`    |
|           | `with`     |
| `->>`     | `yield`    |

### Python Built-in Functions

| ABSI              | Python            |
| ----------------- | ----------------- |
| `\|x\|`           | `abs(x)`          |
|                   | `aiter`           |
| `&:iterable`      | `all(iterable)`   |
|                   | `awaitable anext(async_iterator)` |
| `\|:iterable`     | `any(iterable)`   |
|                   | `ascii(object)`   |
|                   | `bin(x)`          |
| `+-(x)`           | `class bool(x)`   |
| `!!!(*args, **kws)` | `breakpoint(*args, **kws)` |
|                   | `class bytearray(source[, encoding[, errors]])` |
|                   | `bytes([source[, encoding[, errors]]])` |
| `object<-<()={}>` | `callable(object)` |
|                   | `chr(i)`          |
|                   | `@classmethod`    |
|                   | `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)` |
|                   | `complex([real[, imag]])` |
|                   | `delattr(object, name)` |
| `{k v, }`         | `dict(**kwarg)`   |
|                   | `dir([object])`   |
| `a //%% b`        | `divmod(a, b)`    |
| `:(start=0)`      | `enumerate(iterable, start=0)` |
| `!?!(globals=None, locals=None)` | `eval(expression, globals=None, locals=None)` |
| `!?!>>>`          | `exec(source, /, globals=None, locals=None, *, closure=None)` |
| `?`               | `filter(function, iterable)` |
|                   | `float(x)`        |
| `` `{value}` ``   | `format(value[, format_spec])` |
|                   | `frozenset([iterable])` |
|                   | `getattr(object, name[, default])` |
|                   | `globals()`       |
| `object~.name?`   | `hasattr(object, name)` |
|                   | `hash(object)`    |
|                   | `help([object])`  |
|                   | `hex(x)`          |
| `!&object`        | `id(object)`      |
| `.<<`             | `input([prompt])` |
|                   | `int(x)`          |
| `==<`             | `isinstance(object, classinfo)` |
| `>==`             | `issubclass(class, classinfo)` |
| `object.:`        | `iter(object[, sentinel])` |
| `s.:_`            | `len(s)`          |
| `[][:iterable]`   | `list([iterable])` |
|                   | `locals()`       |
| `:function(iterable)` | `map(function, iterable, ...)` |
| `=>:iterable`     | `max(iterable, *[, key, default])` |
| `!&.object`       | `memoryview(object)` |
| `=<:iterable`     | `min(iterable, *[, key, default])` |
| `-<<`             | `next(iterator[, default])` |
| `_`               | `class object`    |
|                   | `oct(x)`          |
| `.<<&`            | `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` |
|                   | `ord(c)`          |
| `^`, `.^`         | `pow(base, exp[, mod])` |
| `.>>`             | `print(*objects, sep=' ', end='\n', file=None, flush=False)` |
|                   | `property(fget=None, fset=None, fdel=None, doc=None)` |
| `:start..step..stop` | `class range([start,] stop[, step])` |
| `.~>>object`      | `repr(object)`    |
| `!:sequence`      | `reversed(sequence)` |
|                   | `round(number[, ndigits])` |
| `{}[:iterable]`   | `class set([iterable])` |
|                   | `setattr(object, name, value)` |
| `<:iterable`, `>:iterable` | `sorted(iterable, /, *, key=None, reverse=False)` |
