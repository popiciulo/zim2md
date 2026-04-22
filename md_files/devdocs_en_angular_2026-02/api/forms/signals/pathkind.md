# PathKind

PathKind



# PathKind

The kind of `FieldPath` (`Root`, `Child` of another `FieldPath`, or `Item` in a `FieldPath` array)

## API

```
type PathKind = PathKind.Root | PathKind.Child | PathKind.Item
```

### PathKind.Root

`interface`

The [`PathKind`](pathkind) for a `FieldPath` that is at the root of its field tree.

```
interface Root {
}
```

### PathKind.Child

`interface`

The [`PathKind`](pathkind) for a `FieldPath` that is a child of another `FieldPath`.

```
interface Child extends PathKind.Root {
}
```

### PathKind.Item

`interface`

The [`PathKind`](pathkind) for a `FieldPath` that is an item in a `FieldPath` array.

```
interface Item extends PathKind.Child {
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/forms/signals/PathKind>
