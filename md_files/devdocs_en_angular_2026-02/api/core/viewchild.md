# viewChild

viewChild



# viewChild

Initializes a view child query.

Consider using [`viewChild.required`](viewchild#required) for queries that should always match.

[Referencing component children with queries](../../guide/components/queries)[Required queries](../../guide/components/queries#required-queries)

## API

```
function viewChild<LocatorT, ReadT>(locator, opts);function viewChild<LocatorT>(locator, opts?);function viewChild.required<LocatorT>(locator, opts?);function viewChild.required<LocatorT, ReadT>(locator, opts);
function viewChild<LocatorT>(locator, opts?);

function viewChild.required<LocatorT>(locator, opts?);
function viewChild.required<LocatorT, ReadT>(locator, opts);
```

```
function viewChild<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<ReadT | undefined>;
```

Initializes a view child query. Consider using [`viewChild.required`](viewchild#required) for queries that should always match.

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<ReadT | undefined>`

```
function viewChild<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { debugName?: string | undefined; } | undefined): Signal<LocatorT | undefined>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ debugName?: string | undefined; } | undefined`

@returns`Signal<LocatorT | undefined>`

```
function viewChild.required<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { debugName?: string | undefined; } | undefined): Signal<LocatorT>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ debugName?: string | undefined; } | undefined`

@returns`Signal<LocatorT>`

```
function viewChild.required<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<ReadT>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<ReadT>`

## Usage Notes

Create a child query in your component by declaring a class field and initializing it with the [`viewChild()`](viewchild) function.

```
@Component({template: '<div #el></div><my-component #cmp />'})
export class TestComponent {
  divEl = viewChild<ElementRef>('el');                   // Signal<ElementRef|undefined>
  divElRequired = viewChild.required<ElementRef>('el');  // Signal<ElementRef>
  cmp = viewChild(MyComponent);                          // Signal<MyComponent|undefined>
  cmpRequired = viewChild.required(MyComponent);         // Signal<MyComponent>
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/viewChild>
