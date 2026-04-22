# TestModuleMetadata

TestModuleMetadata



# TestModuleMetadata

## API

```
interface TestModuleMetadata {
  providers?: any[] | undefined;
  declarations?: any[] | undefined;
  imports?: any[] | undefined;
  schemas?: (any[] | SchemaMetadata)[] | undefined;
  teardown?: ModuleTeardownOptions | undefined;
  errorOnUnknownElements?: boolean | undefined;
  errorOnUnknownProperties?: boolean | undefined;
  rethrowApplicationErrors?: boolean | undefined;
  deferBlockBehavior?: DeferBlockBehavior | undefined;
  inferTagName?: boolean | undefined;
  animationsEnabled?: boolean | undefined;
}
```

### providers

`any[] | undefined`

### declarations

`any[] | undefined`

### imports

`any[] | undefined`

### schemas

`(any[] | SchemaMetadata)[] | undefined`

### teardown

`ModuleTeardownOptions | undefined`

### errorOnUnknownElements

`boolean | undefined`

Whether NG0304 runtime errors should be thrown when unknown elements are present in component's template. Defaults to `false`, where the error is simply logged. If set to `true`, the error is thrown.

### errorOnUnknownProperties

`boolean | undefined`

Whether errors should be thrown when unknown properties are present in component's template. Defaults to `false`, where the error is simply logged. If set to `true`, the error is thrown.

### rethrowApplicationErrors

`boolean | undefined`

Whether errors that happen during application change detection should be rethrown.

When `true`, errors that are caught during application change detection will be reported to the `ErrorHandler` and rethrown to prevent them from going unnoticed in tests.

When `false`, errors are only forwarded to the `ErrorHandler`, which by default simply logs them to the console.

Defaults to `true`.

### deferBlockBehavior

`DeferBlockBehavior | undefined`

Whether defer blocks should behave with manual triggering or play through normally. Defaults to `manual`.

### inferTagName

`boolean | undefined`

Whether to infer the tag name of test components from their selectors. Otherwise `div` will be used as the tag name for test components.

### animationsEnabled

`boolean | undefined`

Whether animate.enter / animate.leave should trigger as normal or be disabled. Defaults to `false`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/TestModuleMetadata>
