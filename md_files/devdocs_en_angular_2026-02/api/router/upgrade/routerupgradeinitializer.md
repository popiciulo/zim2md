# RouterUpgradeInitializer

RouterUpgradeInitializer



# RouterUpgradeInitializer

Creates an initializer that sets up `ngRoute` integration along with setting up the Angular router.

## API

```
const RouterUpgradeInitializer: { provide: InjectionToken<readonly ((compRef: ComponentRef<any>) => void)[]>; multi: boolean; useFactory: () => () => void; };
```

## Usage Notes

For standalone applications:

```
export const appConfig: ApplicationConfig = {
  providers: [RouterUpgradeInitializer],
};
```

For NgModule based applications:

```
@NgModule({
 imports: [
  RouterModule.forRoot(SOME_ROUTES),
  UpgradeModule
],
providers: [
  RouterUpgradeInitializer
]
})
export class AppModule {
  ngDoBootstrap() {}
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/upgrade/RouterUpgradeInitializer>
