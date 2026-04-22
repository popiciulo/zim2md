# provideEnvironmentInitializer

provideEnvironmentInitializer



# provideEnvironmentInitializer

This function is used to provide initialization functions that will be executed upon construction of an environment injector.

[ENVIRONMENT\_INITIALIZER](environment_initializer)

## API

```
function provideEnvironmentInitializer(
  initializerFn: () => void,
): EnvironmentProviders;
```

### provideEnvironmentInitializer

`EnvironmentProviders`

This function is used to provide initialization functions that will be executed upon construction of an environment injector.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`ENVIRONMENT_INITIALIZER`](environment_initializer) token which is now deprecated.

@paraminitializerFn`() => void`

@returns`EnvironmentProviders`

Usage notes

The following example illustrates how to configure an initialization function using [`provideEnvironmentInitializer()`](provideenvironmentinitializer)

```
createEnvironmentInjector(
  [
    provideEnvironmentInitializer(() => {
      console.log('environment initialized');
    }),
  ],
  parentInjector
);
```

## Description

This function is used to provide initialization functions that will be executed upon construction of an environment injector.

Note that the provided initializer is run in the injection context.

Previously, this was achieved using the [`ENVIRONMENT_INITIALIZER`](environment_initializer) token which is now deprecated.

## Usage Notes

The following example illustrates how to configure an initialization function using [`provideEnvironmentInitializer()`](provideenvironmentinitializer)

```
createEnvironmentInjector(
  [
    provideEnvironmentInitializer(() => {
      console.log('environment initialized');
    }),
  ],
  parentInjector
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/provideEnvironmentInitializer>
