# DebugNode

DebugNode



# DebugNode

## API

```
class DebugNode {
  constructor(nativeNode: Node): DebugNode;
  readonly nativeNode: any;
  readonly parent: DebugElement | null;
  readonly injector: Injector;
  readonly componentInstance: any;
  readonly context: any;
  readonly listeners: DebugEventListener[];
  readonly references: { [key: string]: any; };
  readonly providerTokens: any[];
}
```

### constructor

`DebugNode`

@paramnativeNode`Node`

@returns`DebugNode`

### nativeNode

`any`

The underlying DOM node.

### parent

`DebugElement | null`

The [`DebugElement`](debugelement) parent. Will be `null` if this is the root element.

### injector

`Injector`

The host dependency injector. For example, the root element's component instance injector.

### componentInstance

`any`

The element's own component instance, if it has one.

### context

`any`

An object that provides parent context for this element. Often an ancestor component instance that governs this element.

When an element is repeated within \*ngFor, the context is an `NgForOf` whose `$implicit` property is the value of the row instance value. For example, the `hero` in `*ngFor="let hero of heroes"`.

### listeners

`DebugEventListener[]`

The callbacks attached to the component's @Output properties and/or the element's event properties.

### references

`{ [key: string]: any; }`

Dictionary of objects associated with template local variables (e.g. #foo), keyed by the local variable name.

### providerTokens

`any[]`

This component's injector lookup tokens. Includes the component itself plus the tokens that the component lists in its providers metadata.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DebugNode>
