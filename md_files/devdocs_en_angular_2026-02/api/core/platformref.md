# PlatformRef

PlatformRef



# PlatformRef

The Angular platform is the entry point for Angular on a web page. Each page has exactly one platform. Services (such as reflection) which are common to every Angular application running on the page are bound in its scope. A page's platform is initialized implicitly when a platform is created using a platform factory such as `PlatformBrowser`, or explicitly by calling the [`createPlatform()`](createplatform) function.

## API

```
class PlatformRef {
  constructor(_injector: Injector): PlatformRef;
  bootstrapModuleFactory<M>(moduleFactory: NgModuleFactory<M>, options?: (BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; }) | undefined): Promise<NgModuleRef<M>>;
  bootstrapModule<M>(moduleType: Type<M>, compilerOptions?: (CompilerOptions & BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; }) | (CompilerOptions & BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; })[]): Promise<NgModuleRef<M>>;
  onDestroy(callback: () => void): void;
  readonly injector: Injector;
  destroy(): void;
  readonly destroyed: boolean;
}
```

### constructor

`PlatformRef`

@param\_injector`Injector`

@returns`PlatformRef`

### bootstrapModuleFactory

`Promise<NgModuleRef<M>>`

Creates an instance of an [`@NgModule`](ngmodule) for the given platform.

@deprecated

Passing NgModule factories as the [`PlatformRef.bootstrapModuleFactory`](platformref#bootstrapModuleFactory) function argument is deprecated. Use the [`PlatformRef.bootstrapModule`](platformref#bootstrapModule) API instead.

@parammoduleFactory`NgModuleFactory<M>`

@paramoptions`(BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; }) | undefined`

@returns`Promise<NgModuleRef<M>>`

### bootstrapModule

`Promise<NgModuleRef<M>>`

Creates an instance of an [`@NgModule`](ngmodule) for a given platform.

@parammoduleType`Type<M>`

@paramcompilerOptions`(CompilerOptions & BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; }) | (CompilerOptions & BootstrapOptions & { applicationProviders?: (Provider | EnvironmentProviders)[] | undefined; })[]`

@returns`Promise<NgModuleRef<M>>`

Usage notes

### Simple Example

```
@NgModule({
  imports: [BrowserModule]
})
class MyModule {}

let moduleRef = platformBrowser().bootstrapModule(MyModule);
```

### onDestroy

`void`

Registers a listener to be called when the platform is destroyed.

@paramcallback`() => void`

@returns`void`

### injector

`Injector`

Retrieves the platform [`Injector`](injector), which is the parent injector for every Angular application on the page and provides singleton providers.

### destroy

`void`

Destroys the current Angular platform and all Angular applications on the page. Destroys all modules and listeners registered with the platform.

@returns`void`

### destroyed

`boolean`

Indicates whether this instance was destroyed.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/PlatformRef>
