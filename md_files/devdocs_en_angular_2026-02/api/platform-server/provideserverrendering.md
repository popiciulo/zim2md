# provideServerRendering

provideServerRendering



# provideServerRendering

Sets up providers necessary to enable server rendering functionality for the application.

## API

```
function provideServerRendering(): EnvironmentProviders;
```

### provideServerRendering

`EnvironmentProviders`

Sets up providers necessary to enable server rendering functionality for the application.

@returns`EnvironmentProviders`

Usage notes

Basic example of how you can add server support to your application:

```
bootstrapApplication(AppComponent, {
  providers: [provideServerRendering()]
});
```

## Usage Notes

Basic example of how you can add server support to your application:

```
bootstrapApplication(AppComponent, {
  providers: [provideServerRendering()]
});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-server/provideServerRendering>
