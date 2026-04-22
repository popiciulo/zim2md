# HarnessEnvironment

HarnessEnvironment



# HarnessEnvironment

Base harness environment class that can be extended to allow [`ComponentHarness`](componentharness)es to be used in different test environments (e.g. testbed, protractor, etc.). This class implements the functionality of both a [`HarnessLoader`](harnessloader) and [`LocatorFactory`](locatorfactory). This class is generic on the raw element type, `E`, used by the particular test environment.

## API

```
abstract class HarnessEnvironment<E> implements HarnessLoader ,LocatorFactory {
  protected constructor(rawRootElement: E): HarnessEnvironment<E>;
   get rootElement(): TestElement;
  documentRootLocatorFactory(): LocatorFactory;
  locatorFor<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>>;
  locatorForOptional<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T> | null>;
  locatorForAll<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>[]>;
  rootHarnessLoader(): Promise<HarnessLoader>;
  harnessLoaderFor(selector: string): Promise<HarnessLoader>;
  harnessLoaderForOptional(selector: string): Promise<HarnessLoader | null>;
  harnessLoaderForAll(selector: string): Promise<HarnessLoader[]>;
  getHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T>;
  getHarnessOrNull<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T | null>;
  getHarnessAtIndex<T extends ComponentHarness>(query: HarnessQuery<T>, offset: number): Promise<T>;
  getAllHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<T[]>;
  countHarnesses<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<number>;
  hasHarness<T extends ComponentHarness>(query: HarnessQuery<T>): Promise<boolean>;
  getChildLoader(selector: string): Promise<HarnessLoader>;
  getAllChildLoaders(selector: string): Promise<HarnessLoader[]>;
  protected createComponentHarness<T extends ComponentHarness>(harnessType: ComponentHarnessConstructor<T>, element: E): T;
  abstract forceStabilize(): Promise<void>;
  abstract waitForTasksOutsideAngular(): Promise<void>;
  protected abstract getDocumentRoot(): E;
  protected abstract createTestElement(element: E): TestElement;
  protected abstract createEnvironment(element: E): HarnessEnvironment<E>;
  protected abstract getAllRawElements(selector: string): Promise<E[]>;
}
```

### constructor

`HarnessEnvironment<E>`

@paramrawRootElement`E`

The native root element of this [`HarnessEnvironment`](harnessenvironment).

@returns`HarnessEnvironment<E>`

### rootElement

`TestElement`

The root element of this [`HarnessEnvironment`](harnessenvironment) as a [`TestElement`](testelement).

### rootElement

`TestElement`

### documentRootLocatorFactory

`LocatorFactory`

Gets a locator factory rooted at the document root.

@returns`LocatorFactory`

### locatorFor

`() => Promise<LocatorFnResult<T>>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the root element of this [`HarnessEnvironment`](harnessenvironment).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await lf.locatorFor(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await lf.locatorFor('div', DivHarness)() // Gets a `TestElement` instance for #d1
await lf.locatorFor('span')()            // Throws because the `Promise` rejects
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>>`

### locatorForOptional

`() => Promise<LocatorFnResult<T> | null>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the root element of this `HarnessEnvironmnet`.

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
await lf.locatorForOptional(DivHarness, 'div')() // Gets a `DivHarness` instance for #d1
await lf.locatorForOptional('div', DivHarness)() // Gets a `TestElement` instance for #d1
await lf.locatorForOptional('span')()            // Gets `null`
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T> | null>`

### locatorForAll

`() => Promise<LocatorFnResult<T>[]>`

Creates an asynchronous locator function that can be used to find [`ComponentHarness`](componentharness) instances or elements under the root element of this [`HarnessEnvironment`](harnessenvironment).

For example, given the following DOM and assuming `DivHarness.hostSelector` is `'div'` and `IdIsD1Harness.hostSelector` is `'#d1'`

```
<div id="d1"></div><div id="d2"></div>
```

then we expect:

```
// Gets [DivHarness for #d1, TestElement for #d1, DivHarness for #d2, TestElement for #d2]
await lf.locatorForAll(DivHarness, 'div')()
// Gets [TestElement for #d1, TestElement for #d2]
await lf.locatorForAll('div', '#d1')()
// Gets [DivHarness for #d1, IdIsD1Harness for #d1, DivHarness for #d2]
await lf.locatorForAll(DivHarness, IdIsD1Harness)()
// Gets []
await lf.locatorForAll('span')()
```

@paramqueries`T`

A list of queries specifying which harnesses and elements to search for:

- A `string` searches for elements matching the CSS selector specified by the string.
- A [`ComponentHarness`](componentharness) constructor searches for [`ComponentHarness`](componentharness) instances matching the given class.
- A [`HarnessPredicate`](harnesspredicate) searches for [`ComponentHarness`](componentharness) instances matching the given predicate.

@returns`() => Promise<LocatorFnResult<T>[]>`

### rootHarnessLoader

`Promise<HarnessLoader>`

@returns`Promise<HarnessLoader>`

### harnessLoaderFor

`Promise<HarnessLoader>`

Gets a [`HarnessLoader`](harnessloader) instance for an element under the root of this [`HarnessEnvironment`](harnessenvironment).

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader>`

### harnessLoaderForOptional

`Promise<HarnessLoader | null>`

Gets a [`HarnessLoader`](harnessloader) instance for an element under the root of this [`HarnessEnvironment`](harnessenvironment).

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader | null>`

### harnessLoaderForAll

`Promise<HarnessLoader[]>`

Gets a list of [`HarnessLoader`](harnessloader) instances, one for each matching element.

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader[]>`

### getHarness

`Promise<T>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns a [`ComponentHarness`](componentharness) for that instance. If multiple matching components are found, a harness for the first one is returned. If no matching component is found, an error is thrown.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T>`

### getHarnessOrNull

`Promise<T | null>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns a [`ComponentHarness`](componentharness) for that instance. If multiple matching components are found, a harness for the first one is returned. If no matching component is found, null is returned.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T | null>`

### getHarnessAtIndex

`Promise<T>`

Searches for an instance of the component corresponding to the given harness type and index under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns a [`ComponentHarness`](componentharness) for that instance. The index specifies the offset of the component to find. If no matching component is found at that index, an error is thrown.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@paramoffset`number`

@returns`Promise<T>`

### getAllHarnesses

`Promise<T[]>`

Searches for all instances of the component corresponding to the given harness type under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns a list [`ComponentHarness`](componentharness) for each instance.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<T[]>`

### countHarnesses

`Promise<number>`

Searches for all instance of the component corresponding to the given harness type under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns the number that were found.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<number>`

### hasHarness

`Promise<boolean>`

Searches for an instance of the component corresponding to the given harness type under the [`HarnessEnvironment`](harnessenvironment)'s root element, and returns a boolean indicating if any were found.

@paramquery`HarnessQuery<T>`

A query for a harness to create

@returns`Promise<boolean>`

### getChildLoader

`Promise<HarnessLoader>`

Searches for an element with the given selector under the evironment's root element, and returns a [`HarnessLoader`](harnessloader) rooted at the matching element. If multiple elements match the selector, the first is used. If no elements match, an error is thrown.

@paramselector`string`

The selector for the root element of the new [`HarnessLoader`](harnessloader)

@returns`Promise<HarnessLoader>`

### getAllChildLoaders

`Promise<HarnessLoader[]>`

Searches for all elements with the given selector under the environment's root element, and returns an array of [`HarnessLoader`](harnessloader)s, one for each matching element, rooted at that element.

@paramselector`string`

The selector for the root element of the new [`HarnessLoader`](harnessloader)

@returns`Promise<HarnessLoader[]>`

### createComponentHarness

`T`

Creates a [`ComponentHarness`](componentharness) for the given harness type with the given raw host element.

@paramharnessType`ComponentHarnessConstructor<T>`

@paramelement`E`

@returns`T`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks captured in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events. This is an abstrct method that must be implemented by subclasses.

@returns`Promise<void>`

### waitForTasksOutsideAngular

`Promise<void>`

Waits for all scheduled or running async tasks to complete. This allows harness authors to wait for async tasks outside of the Angular zone. This is an abstrct method that must be implemented by subclasses.

@returns`Promise<void>`

### getDocumentRoot

`E`

Gets the root element for the document.

@returns`E`

### createTestElement

`TestElement`

Creates a [`TestElement`](testelement) from a raw element.

@paramelement`E`

@returns`TestElement`

### createEnvironment

`HarnessEnvironment<E>`

Creates a [`HarnessEnvironment`](harnessenvironment) rooted at the given raw element.

@paramelement`E`

@returns`HarnessEnvironment<E>`

### getAllRawElements

`Promise<E[]>`

Gets a list of all elements matching the given selector under this environment's root element.

@paramselector`string`

@returns`Promise<E[]>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/HarnessEnvironment>
