# LocatorFnResult

LocatorFnResult



# LocatorFnResult

The result type obtained when searching using a particular list of queries. This type depends on the particular items being queried.

- If one of the queries is for a `ComponentHarnessConstructor<C1>`, it means that the result might be a harness of type `C1`
- If one of the queries is for a `HarnessPredicate<C2>`, it means that the result might be a harness of type `C2`
- If one of the queries is for a `string`, it means that the result might be a [`TestElement`](testelement).

## API

```
type LocatorFnResult<T extends (HarnessQuery<any> | string)[]> = {
  [I in keyof T]: T[I] extends new (...args: any[]) => infer C // Map `ComponentHarnessConstructor<C>` to `C`.
    ? C
    : // Map `HarnessPredicate<C>` to `C`.
      T[I] extends {harnessType: new (...args: any[]) => infer C}
      ? C
      : // Map `string` to `TestElement`.
        T[I] extends string
        ? TestElement
        : // Map everything else to `never` (should not happen due to the type constraint on `T`).
          never;
}[number]
```

## Description

The result type obtained when searching using a particular list of queries. This type depends on the particular items being queried.

- If one of the queries is for a `ComponentHarnessConstructor<C1>`, it means that the result might be a harness of type `C1`
- If one of the queries is for a `HarnessPredicate<C2>`, it means that the result might be a harness of type `C2`
- If one of the queries is for a `string`, it means that the result might be a [`TestElement`](testelement).

Since we don't know for sure which query will match, the result type if the union of the types for all possible results.

## Usage Notes

### Example

The type:

```
LocatorFnResult<[
  ComponentHarnessConstructor<MyHarness>,
  HarnessPredicate<MyOtherHarness>,
  string
]>
```

is equivalent to:

```
MyHarness | MyOtherHarness | TestElement
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/cdk/testing/LocatorFnResult>
