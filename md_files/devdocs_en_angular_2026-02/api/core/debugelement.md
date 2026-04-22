# DebugElement

DebugElement



# DebugElement

[Component testing scenarios](../../guide/testing/components-scenarios)[Basics of testing components](../../guide/testing/components-basics)[Testing utility APIs](../../guide/testing/utility-apis)

## API

```
class DebugElement extends DebugNode {
  constructor(nativeNode: Element): DebugElement;
  readonly nativeElement: any;
  readonly name: string;
  readonly properties: { [key: string]: any; };
  readonly attributes: { [key: string]: string | null; };
  readonly styles: { [key: string]: string | null; };
  readonly classes: { [key: string]: boolean; };
  readonly childNodes: DebugNode[];
  readonly children: DebugElement[];
  query(predicate: Predicate<DebugElement>): DebugElement;
  queryAll(predicate: Predicate<DebugElement>): DebugElement[];
  queryAllNodes(predicate: Predicate<DebugNode>): DebugNode[];
  triggerEventHandler(eventName: string, eventObj?: any): void;
  readonly override nativeNode: any;
  override readonly parent: DebugElement | null;
  override readonly injector: Injector;
  override readonly componentInstance: any;
  override readonly context: any;
  override readonly listeners: DebugEventListener[];
  override readonly references: { [key: string]: any; };
  override readonly providerTokens: any[];
}
```

### constructor

`DebugElement`

@paramnativeNode`Element`

@returns`DebugElement`

### nativeElement

`any`

The underlying DOM element at the root of the component.

### name

`string`

The element tag name, if it is an element.

### properties

`{ [key: string]: any; }`

Gets a map of property names to property values for an element.

This map includes:

- Regular property bindings (e.g. `[id]="id"`)
- Host property bindings (e.g. `host: { '[id]': "id" }`)
- Interpolated property bindings (e.g. `id="{{ value }}")

It does not include:

- input property bindings (e.g. `[myCustomInput]="value"`)
- attribute bindings (e.g. `[attr.role]="menu"`)

### attributes

`{ [key: string]: string | null; }`

A map of attribute names to attribute values for an element.

### styles

`{ [key: string]: string | null; }`

The inline styles of the DOM element.

### classes

`{ [key: string]: boolean; }`

A map containing the class names on the element as keys.

This map is derived from the `className` property of the DOM element.

Note: The values of this object will always be `true`. The class key will not appear in the KV object if it does not exist on the element.

### childNodes

`DebugNode[]`

The `childNodes` of the DOM element as a [`DebugNode`](debugnode) array.

### children

`DebugElement[]`

The immediate [`DebugElement`](debugelement) children. Walk the tree by descending through `children`.

### query

`DebugElement`

@parampredicate`Predicate<DebugElement>`

@returns`DebugElement`

### queryAll

`DebugElement[]`

@parampredicate`Predicate<DebugElement>`

@returns`DebugElement[]`

### queryAllNodes

`DebugNode[]`

@parampredicate`Predicate<DebugNode>`

@returns`DebugNode[]`

### triggerEventHandler

`void`

Triggers the event by its name if there is a corresponding listener in the element's `listeners` collection.

If the event lacks a listener or there's some other problem, consider calling `nativeElement.dispatchEvent(eventObject)`.

@parameventName`string`

The name of the event to trigger

@parameventObj`any`

The *event object* expected by the handler

@returns`void`

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
<https://angular.dev/api/core/DebugElement>
