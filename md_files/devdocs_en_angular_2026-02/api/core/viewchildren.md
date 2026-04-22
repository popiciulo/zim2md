# viewChildren

viewChildren



# viewChildren

Initializes a view children query.

Query results are represented as a signal of a read-only collection containing all matched elements.

[Referencing component children with queries](../../guide/components/queries)[Required queries](../../guide/components/queries#required-queries)

## API

```
function viewChildren<LocatorT>(locator, opts?);function viewChildren<LocatorT, ReadT>(locator, opts);
function viewChildren<LocatorT, ReadT>(locator, opts);
```

```
function viewChildren<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { debugName?: string | undefined; } | undefined): Signal<readonly LocatorT[]>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ debugName?: string | undefined; } | undefined`

@returns`Signal<readonly LocatorT[]>`

```
function viewChildren<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<readonly ReadT[]>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<readonly ReadT[]>`

## Usage Notes

Create a children query in your component by declaring a class field and initializing it with the [`viewChildren()`](viewchildren) function.

```
@Component({...})
export class TestComponent {
  divEls = viewChildren<ElementRef>('el');   // Signal<ReadonlyArray<ElementRef>>
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/viewChildren>
