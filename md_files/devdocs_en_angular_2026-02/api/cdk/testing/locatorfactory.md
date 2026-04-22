# LocatorFactory

LocatorFactory



# LocatorFactory

Interface used to create asynchronous locator functions used find elements and component harnesses. This interface is used by [`ComponentHarness`](componentharness) authors to create locator functions for their [`ComponentHarness`](componentharness) subclass.

## API

```
interface LocatorFactory {
  documentRootLocatorFactory(): LocatorFactory;
  rootElement: TestElement;
  locatorFor<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>>;
  locatorForOptional<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T> | null>;
  locatorForAll<T extends (HarnessQuery<any> | string)[]>(...queries: T): () => Promise<LocatorFnResult<T>[]>;
  rootHarnessLoader(): Promise<HarnessLoader>;
  harnessLoaderFor(selector: string): Promise<HarnessLoader>;
  harnessLoaderForOptional(selector: string): Promise<HarnessLoader | null>;
  harnessLoaderForAll(selector: string): Promise<HarnessLoader[]>;
  forceStabilize(): Promise<void>;
  waitForTasksOutsideAngular(): Promise<void>;
}
```

### documentRootLocatorFactory

`LocatorFactory`

Gets a locator factory rooted at the document root.

@returns`LocatorFactory`

### rootElement

`TestElement`

The root element of this [`LocatorFactory`](locatorfactory) as a [`TestElement`](testelement).

### locatorFor

`() => Promise<LocatorFnResult<T>>`

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the root element of this [`LocatorFactory`](locatorfactory).

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

Creates an asynchronous locator function that can be used to find a [`ComponentHarness`](componentharness) instance or element under the root element of this [`LocatorFactory`](locatorfactory).

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

Creates an asynchronous locator function that can be used to find [`ComponentHarness`](componentharness) instances or elements under the root element of this [`LocatorFactory`](locatorfactory).

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

Gets a [`HarnessLoader`](harnessloader) instance for an element under the root of this [`LocatorFactory`](locatorfactory).

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader>`

### harnessLoaderForOptional

`Promise<HarnessLoader | null>`

Gets a [`HarnessLoader`](harnessloader) instance for an element under the root of this [`LocatorFactory`](locatorfactory)

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader | null>`

### harnessLoaderForAll

`Promise<HarnessLoader[]>`

Gets a list of [`HarnessLoader`](harnessloader) instances, one for each matching element.

@paramselector`string`

The selector for the root element.

@returns`Promise<HarnessLoader[]>`

### forceStabilize

`Promise<void>`

Flushes change detection and async tasks captured in the Angular zone. In most cases it should not be necessary to call this manually. However, there may be some edge cases where it is needed to fully flush animation events.

@returns`Promise<void>`

### waitForTasksOutsideAngular

`Promise<void>`

Waits for all scheduled or running async tasks to complete. This allows harness authors to wait for async tasks outside of the Angular zone.

@returns`Promise<void>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/LocatorFactory>
