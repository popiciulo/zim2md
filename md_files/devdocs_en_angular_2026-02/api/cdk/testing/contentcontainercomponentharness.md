# ContentContainerComponentHarness

ContentContainerComponentHarness



# ContentContainerComponentHarness

Base class for component harnesses that authors should extend if they anticipate that consumers of the harness may want to access other harnesses within the `<ng-content>` of the component.

## API

```
abstract class ContentContainerComponentHarness<S extends string = string> extends ComponentHarness implements HarnessLoader {
  getChildLoader(selector: S): Promise<HarnessLoader>;
  getAllChildLoaders(selector: S): Promise<HarnessLoader[]>;
  getHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T>;
  getHarnessOrNull<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T | null>;
  getHarnessAtIndex<T extends ComponentHarness>(query: HarnessQuery<T>, index: number): Promise<T>;
  getAllHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T[]>;
  countHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<number>;
  hasHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<boolean>;
  protected getRootHarnessLoader(): Promise<HarnessLoader>;
  override host(): Promise<TestElement>;
  protected override documentRootLocatorFactory(): LocatorFactory;
  protected override locatorFor<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>>;
  protected override locatorForOptional<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T> | null>;
  protected override locatorForAll<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>[]>;
  protected override forceStabilize(): Promise<void>;
  protected override waitForTasksOutsideAngular(): Promise<void>;
}
```

### getChildLoader

`Promise<HarnessLoader>`

Gets a [`HarnessLoader`](harnessloader) that searches for harnesses under the first element matching the given selector within the current harness's content.

@paramselector`S`

The selector for an element in the component's content.

@returns`Promise<HarnessLoader>`

### getAllChildLoaders

`Promise<HarnessLoader[]>`

Gets a list of [`HarnessLoader`](harnessloader) for each element matching the given selector under the current harness's cotnent that searches for harnesses under that element.

@paramselector`S`

The selector for elements in the component's content.

@returns`Promise<HarnessLoader[]>`

### getHarness

`Promise<T>`

Gets the first matching harness for the given query within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@returns`Promise<T>`

### getHarnessOrNull

`Promise<T | null>`

Gets the first matching harness for the given query within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@returns`Promise<T | null>`

### getHarnessAtIndex

`Promise<T>`

Gets a matching harness for the given query and index within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@paramindex`number`

The zero-indexed offset of the component to find.

@returns`Promise<T>`

### getAllHarnesses

`Promise<T[]>`

Gets all matching harnesses for the given query within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@returns`Promise<T[]>`

### countHarnesses

`Promise<number>`

Returns the number of matching harnesses for the given query within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@returns`Promise<number>`

### hasHarness

`Promise<boolean>`

Checks whether there is a matching harnesses for the given query within the current harness's content.

@paramquery`HarnessQuery<T>`

The harness query to search for.

@returns`Promise<boolean>`

### getRootHarnessLoader

`Promise<HarnessLoader>`

Gets the root harness loader from which to start searching for content contained by this harness.

@returns`Promise<HarnessLoader>`

### host

`Promise<TestElement>`

Gets a `Promise` for the [`TestElement`](testelement) representing the host element of the component.

@returns`Promise<TestElement>`

### documentRootLocatorFactory

`LocatorFactory`

Gets a [`LocatorFactory`](locatorfactory) for the document root element. This factory can be used to create locators for elements that a component creates outside of its own root element. (e.g. by appending to document.body).

@returns`LocatorFactory`

### locatorFor

`() => Promise<LocatorFnResult<T>>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await ch.locatorFor(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await ch.locatorFor('div', DivHarness)() // Gets a `TestElement` instance for #d1
await ch.locatorFor('span')()            // Throws because the `Promise` rejects
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>>`

### locatorForOptional

`() => Promise<LocatorFnResult<T> | null>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await ch.locatorForOptional(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await ch.locatorForOptional('div', DivHarness)() // Gets a `TestElement` instance for #d1
await ch.locatorForOptional('span')()            // Gets `null`
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T> | null>`

### locatorForAll

`() => Promise<LocatorFnResult<T>[]>`

Creates an asynchronous locator function that can be used to find [`ComponentHarness`](componentharness) instances or elements under the host element of this [`ComponentHarness`](componentharness).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'` and `IdIsD1Harness.hostSelector` is `'#d1'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
// Gets [DivHarness for #d1, TestElement for #d1, DivHarness for #d2, TestElement for #d2]
await ch.locatorForAll(DivHarness, 'div')()
// Gets [TestElement for #d1, TestElement for #d2]
await ch.locatorForAll('div', '#d1')()
// Gets [DivHarness for #d1, IdIsD1Harness for #d1, DivHarness for #d2]
await ch.locatorForAll(DivHarness, IdIsD1Harness)()
// Gets []
await ch.locatorForAll('span')()
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>[]>`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events.

@returns`Promise<void>`

### waitForTasksOutsideAngular

`Promise<void>`

Waits for all scheduled or running async tasks to complete. This allows harness authors to wait for async tasks outside of the Angular zone.

@returns`Promise<void>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/ContentContainerComponentHarness>
