# contentChild

contentChild



# contentChild

Initializes a content child query. Consider using [`contentChild.required`](contentchild#required) for queries that should always match.

## API

```
function contentChild<LocatorT>(locator, opts?);function contentChild<LocatorT, ReadT>(locator, opts);function contentChild.required<LocatorT>(locator, opts?);function contentChild.required<LocatorT, ReadT>(locator, opts);
function contentChild<LocatorT, ReadT>(locator, opts);

function contentChild.required<LocatorT>(locator, opts?);
function contentChild.required<LocatorT, ReadT>(locator, opts);
```

```
function contentChild<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined): Signal<LocatorT | undefined>;
```

Initializes a content child query.

Consider using [`contentChild.required`](contentchild#required) for queries that should always match.

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined`

@returns`Signal<LocatorT | undefined>`

```
function contentChild<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<ReadT | undefined>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<ReadT | undefined>`

```
function contentChild.required<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined): Signal<LocatorT>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined`

@returns`Signal<LocatorT>`

```
function contentChild.required<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<ReadT>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<ReadT>`

## Usage Notes

Create a child query in your component by declaring a class field and initializing it with the [`contentChild()`](contentchild) function.

```
@Component({...})
export class TestComponent {
  headerEl = contentChild<ElementRef>('h');                    // Signal<ElementRef|undefined>
  headerElElRequired = contentChild.required<ElementRef>('h'); // Signal<ElementRef>
  header = contentChild(MyHeader);                             // Signal<MyHeader|undefined>
  headerRequired = contentChild.required(MyHeader);            // Signal<MyHeader>
}
```

Note: By default `descendants` is `true` which means the query will traverse all descendants in the same template.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/contentChild>
