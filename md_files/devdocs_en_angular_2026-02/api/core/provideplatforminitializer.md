# providePlatformInitializer

providePlatformInitializer



# providePlatformInitializer

This function is used to provide initialization functions that will be executed upon initialization of the platform injector.

[PLATFORM\_INITIALIZER](platform_initializer)

## API

```
function providePlatformInitializer(
  initializerFn: () => void,
): EnvironmentProviders;
```

### providePlatformInitializer

`EnvironmentProviders`

This function is used to provide initialization functions that will be executed upon initialization of the platform injector.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`PLATFORM_INITIALIZER`](platform_initializer) token which is now deprecated.

@paraminitializerFn`() => void`

@returns`EnvironmentProviders`

## Description

This function is used to provide initialization functions that will be executed upon initialization of the platform injector.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`PLATFORM_INITIALIZER`](platform_initializer) token which is now deprecated.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/providePlatformInitializer>
