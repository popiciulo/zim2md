# TestBed

TestBed



# TestBed

## API

```
interface TestBed {
  readonly platform: PlatformRef;
  readonly ngModule: Type<any> | Type<any>[];
  initTestEnvironment(ngModule: Type<any> | Type<any>[], platform: PlatformRef, options?: TestEnvironmentOptions | undefined): void;
  resetTestEnvironment(): void;
  resetTestingModule(): TestBed;
  configureCompiler(config: { providers?: any[] | undefined; useJit?: boolean | undefined; }): void;
  configureTestingModule(moduleDef: TestModuleMetadata): TestBed;
  compileComponents(): Promise<any>;
  inject<T>(token: ProviderToken<T>, notFoundValue: undefined, options: InjectOptions & { optional?: false | undefined; }): T;
  inject<T>(token: ProviderToken<T>, notFoundValue: null | undefined, options: InjectOptions): T | null;
  inject<T>(token: ProviderToken<T>, notFoundValue?: T | undefined, options?: InjectOptions | undefined): T;
  runInInjectionContext<T>(fn: () => T): T;
  execute(tokens: any[], fn: Function, context?: any): any;
  overrideModule(ngModule: Type<any>, override: MetadataOverride<NgModule>): TestBed;
  overrideComponent(component: Type<any>, override: MetadataOverride<Component>): TestBed;
  overrideDirective(directive: Type<any>, override: MetadataOverride<Directive>): TestBed;
  overridePipe(pipe: Type<any>, override: MetadataOverride<Pipe>): TestBed;
  overrideTemplate(component: Type<any>, template: string): TestBed;
  overrideProvider(token: any, provider: { useFactory: Function; deps: any[]; multi?: boolean | undefined; }): TestBed;
  overrideProvider(token: any, provider: { useValue: any; multi?: boolean | undefined; }): TestBed;
  overrideProvider(token: any, provider: { useFactory?: Function | undefined; useValue?: any; deps?: any[] | undefined; multi?: boolean | undefined; }): TestBed;
  overrideTemplateUsingTestingModule(component: Type<any>, template: string): TestBed;
  createComponent<T>(component: Type<T>, options?: TestComponentOptions | undefined): ComponentFixture<T>;
  flushEffects(): void;
  tick(): void;
  readonly platform: PlatformRef;
  readonly ngModule: Type<any> | Type<any>[];
  initTestEnvironment(ngModule: Type<any> | Type<any>[], platform: PlatformRef, options?: TestEnvironmentOptions | undefined): void;
  resetTestEnvironment(): void;
  resetTestingModule(): TestBed;
  configureCompiler(config: { providers?: any[] | undefined; useJit?: boolean | undefined; }): void;
  configureTestingModule(moduleDef: TestModuleMetadata): TestBed;
  compileComponents(): Promise<any>;
  inject<T>(token: ProviderToken<T>, notFoundValue: undefined, options: InjectOptions & { optional?: false | undefined; }): T;
  inject<T>(token: ProviderToken<T>, notFoundValue: null | undefined, options: InjectOptions): T | null;
  inject<T>(token: ProviderToken<T>, notFoundValue?: T | undefined, options?: InjectOptions | undefined): T;
  runInInjectionContext<T>(fn: () => T): T;
  execute(tokens: any[], fn: Function, context?: any): any;
  overrideModule(ngModule: Type<any>, override: MetadataOverride<NgModule>): TestBed;
  overrideComponent(component: Type<any>, override: MetadataOverride<Component>): TestBed;
  overrideDirective(directive: Type<any>, override: MetadataOverride<Directive>): TestBed;
  overridePipe(pipe: Type<any>, override: MetadataOverride<Pipe>): TestBed;
  overrideTemplate(component: Type<any>, template: string): TestBed;
  overrideProvider(token: any, provider: { useFactory: Function; deps: any[]; multi?: boolean | undefined; }): TestBed;
  overrideProvider(token: any, provider: { useValue: any; multi?: boolean | undefined; }): TestBed;
  overrideProvider(token: any, provider: { useFactory?: Function | undefined; useValue?: any; deps?: any[] | undefined; multi?: boolean | undefined; }): TestBed;
  overrideTemplateUsingTestingModule(component: Type<any>, template: string): TestBed;
  createComponent<T>(component: Type<T>, options?: TestComponentOptions | undefined): ComponentFixture<T>;
  flushEffects(): void;
  tick(): void;
}
```

### platform

`PlatformRef`

### ngModule

`Type<any> | Type<any>[]`

### initTestEnvironment

`void`

Initialize the environment for testing with a compiler factory, a PlatformRef, and an angular module. These are common to every test in the suite.

This may only be called once, to set up the common providers for the current test suite on the current platform. If you absolutely need to change the providers, first use `resetTestEnvironment`.

Test modules and platforms for individual platforms are available from '@angular//testing'.

@paramngModule`Type<any> | Type<any>[]`

@paramplatform`PlatformRef`

@paramoptions`TestEnvironmentOptions | undefined`

@returns`void`

### resetTestEnvironment

`void`

Reset the providers for the test injector.

@returns`void`

### resetTestingModule

`TestBed`

@returns`TestBed`

### configureCompiler

`void`

@paramconfig`{ providers?: any[] | undefined; useJit?: boolean | undefined; }`

@returns`void`

### configureTestingModule

`TestBed`

@parammoduleDef`TestModuleMetadata`

@returns`TestBed`

### compileComponents

`Promise<any>`

@returns`Promise<any>`

### inject

`T`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`undefined`

@paramoptions`InjectOptions & { optional?: false | undefined; }`

@returns`T`

### inject

`T | null`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`null | undefined`

@paramoptions`InjectOptions`

@returns`T | null`

### inject

`T`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`T | undefined`

@paramoptions`InjectOptions | undefined`

@returns`T`

### runInInjectionContext

`T`

Runs the given function in the `EnvironmentInjector` context of [`TestBed`](testbed).

@paramfn`() => T`

@returns`T`

### execute

`any`

@paramtokens`any[]`

@paramfn`Function`

@paramcontext`any`

@returns`any`

### overrideModule

`TestBed`

@paramngModule`Type<any>`

@paramoverride`MetadataOverride<NgModule>`

@returns`TestBed`

### overrideComponent

`TestBed`

@paramcomponent`Type<any>`

@paramoverride`MetadataOverride<Component>`

@returns`TestBed`

### overrideDirective

`TestBed`

@paramdirective`Type<any>`

@paramoverride`MetadataOverride<Directive>`

@returns`TestBed`

### overridePipe

`TestBed`

@parampipe`Type<any>`

@paramoverride`MetadataOverride<Pipe>`

@returns`TestBed`

### overrideTemplate

`TestBed`

@paramcomponent`Type<any>`

@paramtemplate`string`

@returns`TestBed`

### overrideProvider

`TestBed`

Overwrites all providers for the given token with the given provider definition.

@paramtoken`any`

@paramprovider`{ useFactory: Function; deps: any[]; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideProvider

`TestBed`

@paramtoken`any`

@paramprovider`{ useValue: any; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideProvider

`TestBed`

@paramtoken`any`

@paramprovider`{ useFactory?: Function | undefined; useValue?: any; deps?: any[] | undefined; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideTemplateUsingTestingModule

`TestBed`

@paramcomponent`Type<any>`

@paramtemplate`string`

@returns`TestBed`

### createComponent

`ComponentFixture<T>`

@paramcomponent`Type<T>`

@paramoptions`TestComponentOptions | undefined`

@returns`ComponentFixture<T>`

### flushEffects

`void`

Execute any pending effects.

@deprecated

use [`TestBed.tick()`](testbed#tick) instead

@returns`void`

### tick

`void`

Execute any pending work required to synchronize model to the UI.

@returns`void`

### platform

`PlatformRef`

### ngModule

`Type<any> | Type<any>[]`

### initTestEnvironment

`void`

Initialize the environment for testing with a compiler factory, a PlatformRef, and an angular module. These are common to every test in the suite.

This may only be called once, to set up the common providers for the current test suite on the current platform. If you absolutely need to change the providers, first use `resetTestEnvironment`.

Test modules and platforms for individual platforms are available from '@angular//testing'.

@paramngModule`Type<any> | Type<any>[]`

@paramplatform`PlatformRef`

@paramoptions`TestEnvironmentOptions | undefined`

@returns`void`

### resetTestEnvironment

`void`

Reset the providers for the test injector.

@returns`void`

### resetTestingModule

`TestBed`

@returns`TestBed`

### configureCompiler

`void`

@paramconfig`{ providers?: any[] | undefined; useJit?: boolean | undefined; }`

@returns`void`

### configureTestingModule

`TestBed`

@parammoduleDef`TestModuleMetadata`

@returns`TestBed`

### compileComponents

`Promise<any>`

@returns`Promise<any>`

### inject

`T`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`undefined`

@paramoptions`InjectOptions & { optional?: false | undefined; }`

@returns`T`

### inject

`T | null`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`null | undefined`

@paramoptions`InjectOptions`

@returns`T | null`

### inject

`T`

@paramtoken`ProviderToken<T>`

@paramnotFoundValue`T | undefined`

@paramoptions`InjectOptions | undefined`

@returns`T`

### runInInjectionContext

`T`

Runs the given function in the `EnvironmentInjector` context of [`TestBed`](testbed).

@paramfn`() => T`

@returns`T`

### execute

`any`

@paramtokens`any[]`

@paramfn`Function`

@paramcontext`any`

@returns`any`

### overrideModule

`TestBed`

@paramngModule`Type<any>`

@paramoverride`MetadataOverride<NgModule>`

@returns`TestBed`

### overrideComponent

`TestBed`

@paramcomponent`Type<any>`

@paramoverride`MetadataOverride<Component>`

@returns`TestBed`

### overrideDirective

`TestBed`

@paramdirective`Type<any>`

@paramoverride`MetadataOverride<Directive>`

@returns`TestBed`

### overridePipe

`TestBed`

@parampipe`Type<any>`

@paramoverride`MetadataOverride<Pipe>`

@returns`TestBed`

### overrideTemplate

`TestBed`

@paramcomponent`Type<any>`

@paramtemplate`string`

@returns`TestBed`

### overrideProvider

`TestBed`

Overwrites all providers for the given token with the given provider definition.

@paramtoken`any`

@paramprovider`{ useFactory: Function; deps: any[]; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideProvider

`TestBed`

@paramtoken`any`

@paramprovider`{ useValue: any; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideProvider

`TestBed`

@paramtoken`any`

@paramprovider`{ useFactory?: Function | undefined; useValue?: any; deps?: any[] | undefined; multi?: boolean | undefined; }`

@returns`TestBed`

### overrideTemplateUsingTestingModule

`TestBed`

@paramcomponent`Type<any>`

@paramtemplate`string`

@returns`TestBed`

### createComponent

`ComponentFixture<T>`

@paramcomponent`Type<T>`

@paramoptions`TestComponentOptions | undefined`

@returns`ComponentFixture<T>`

### flushEffects

`void`

Execute any pending effects.

@deprecated

use [`TestBed.tick()`](testbed#tick) instead

@returns`void`

### tick

`void`

Execute any pending work required to synchronize model to the UI.

@returns`void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/testing/TestBed>
