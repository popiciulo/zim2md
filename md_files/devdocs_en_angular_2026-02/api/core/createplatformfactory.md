# createPlatformFactory

createPlatformFactory



# createPlatformFactory

Creates a factory for a platform. Can be used to provide or override `Providers` specific to your application's runtime needs, such as [`PLATFORM_INITIALIZER`](platform_initializer) and [`PLATFORM_ID`](platform_id).

## API

```
function createPlatformFactory(
  parentPlatformFactory:
    | ((extraProviders?: StaticProvider[] | undefined) => PlatformRef)
    | null,
  name: string,
  providers?: StaticProvider[],
): (extraProviders?: StaticProvider[] | undefined) => PlatformRef;
```

### createPlatformFactory

`(extraProviders?: StaticProvider[] | undefined) => PlatformRef`

Creates a factory for a platform. Can be used to provide or override `Providers` specific to your application's runtime needs, such as [`PLATFORM_INITIALIZER`](platform_initializer) and [`PLATFORM_ID`](platform_id).

@paramparentPlatformFactory`((extraProviders?: StaticProvider[] | undefined) => PlatformRef) | null`

Another platform factory to modify. Allows you to compose factories to build up configurations that might be required by different libraries or parts of the application.

@paramname`string`

Identifies the new platform factory.

@paramproviders`StaticProvider[]`

A set of dependency providers for platforms created with the new factory.

@returns`(extraProviders?: StaticProvider[] | undefined) => PlatformRef`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/createPlatformFactory>
