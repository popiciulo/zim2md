# contentChildren

contentChildren



# contentChildren

Initializes a content children query.

Query results are represented as a signal of a read-only collection containing all matched elements.

[Referencing component children with queries](../../guide/components/queries)[Content queries](../../guide/components/queries#content-queries)

## API

```
function contentChildren<LocatorT>(locator, opts?);function contentChildren<LocatorT, ReadT>(locator, opts);
function contentChildren<LocatorT, ReadT>(locator, opts);
```

```
function contentChildren<LocatorT>(locator: string | ProviderToken<LocatorT>, opts?: { descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined): Signal<readonly LocatorT[]>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read?: undefined; debugName?: string | undefined; } | undefined`

@returns`Signal<readonly LocatorT[]>`

```
function contentChildren<LocatorT, ReadT>(locator: string | ProviderToken<LocatorT>, opts: { descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }): Signal<readonly ReadT[]>;
```

@paramlocator`string | ProviderToken<LocatorT>`

@paramopts`{ descendants?: boolean | undefined; read: ProviderToken<ReadT>; debugName?: string | undefined; }`

@returns`Signal<readonly ReadT[]>`

## Usage Notes

Create a children query in your component by declaring a class field and initializing it with the [`contentChildren()`](contentchildren) function.

```
@Component({...})
export class TestComponent {
  headerEl = contentChildren<ElementRef>('h');   // Signal<ReadonlyArray<ElementRef>>
}
```

Note: By default `descendants` is `false` which means the query will not traverse all descendants in the same template.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/contentChildren>
