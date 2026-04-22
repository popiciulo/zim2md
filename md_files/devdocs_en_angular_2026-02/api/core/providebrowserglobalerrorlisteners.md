# provideBrowserGlobalErrorListeners

provideBrowserGlobalErrorListeners



# provideBrowserGlobalErrorListeners

Provides an environment initializer which forwards unhandled errors to the ErrorHandler.

[Global error listeners](https://angular.dev/best-practices/error-handling#global-error-listeners)

## API

```
function provideBrowserGlobalErrorListeners(): EnvironmentProviders;
```

### provideBrowserGlobalErrorListeners

`EnvironmentProviders`

Provides an environment initializer which forwards unhandled errors to the ErrorHandler.

The listeners added are for the window's 'unhandledrejection' and 'error' events.

@returns`EnvironmentProviders`

## Description

Provides an environment initializer which forwards unhandled errors to the ErrorHandler.

The listeners added are for the window's 'unhandledrejection' and 'error' events.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/provideBrowserGlobalErrorListeners>
