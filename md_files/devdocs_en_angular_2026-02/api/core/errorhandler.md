# ErrorHandler

ErrorHandler



# ErrorHandler

Provides a hook for centralized exception handling.

[Unhandled errors in Angular](https://angular.dev/best-practices/error-handling)

## API

```
class ErrorHandler {
  handleError(error: any): void;
}
```

### handleError

`void`

@paramerror`any`

@returns`void`

## Description

Provides a hook for centralized exception handling.

The default implementation of [`ErrorHandler`](errorhandler) prints error messages to the `console`. To intercept error handling, write a custom exception handler that replaces this default as appropriate for your app.

## Usage Notes

### Example

```
class MyErrorHandler implements ErrorHandler {
  handleError(error) {
    // do something with the exception
  }
}

// Provide in standalone apps
bootstrapApplication(AppComponent, {
  providers: [{provide: ErrorHandler, useClass: MyErrorHandler}]
})

// Provide in module-based apps
@NgModule({
  providers: [{provide: ErrorHandler, useClass: MyErrorHandler}]
})
class MyModule {}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ErrorHandler>
