# By

By



# By

Predicates for use with [`DebugElement`](../core/debugelement)'s query functions.

## API

```
class By {
  static all(): Predicate<DebugNode>;
  static css(selector: string): Predicate<DebugElement>;
  static directive(type: Type<any>): Predicate<DebugNode>;
}
```

### all

`Predicate<DebugNode>`

Match all nodes.

@returns`Predicate<DebugNode>`

Usage notes

### Example

```
debugElement.query(By.all());
```

### css

`Predicate<DebugElement>`

Match elements by the given CSS selector.

@paramselector`string`

@returns`Predicate<DebugElement>`

Usage notes

### Example

```
debugElement.query(By.css('[attribute]'));
```

### directive

`Predicate<DebugNode>`

Match nodes that have the given directive present.

@paramtype`Type<any>`

@returns`Predicate<DebugNode>`

Usage notes

### Example

```
debugElement.query(By.directive(MyDirective));
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/By>
