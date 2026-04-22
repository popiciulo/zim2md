# APP_ID

APP\_ID



# APP\_ID

A DI token representing a string ID, used primarily for prefixing application attributes and CSS styles when [`ViewEncapsulation#Emulated`](viewencapsulation#Emulated) is being used.

## API

```
const APP_ID: InjectionToken<string>;
```

## Description

A DI token representing a string ID, used primarily for prefixing application attributes and CSS styles when [`ViewEncapsulation#Emulated`](viewencapsulation#Emulated) is being used.

The token is needed in cases when multiple applications are bootstrapped on a page (for example, using `bootstrapApplication` calls). In this case, ensure that those applications have different [`APP_ID`](app_id) value setup. For example:

```
bootstrapApplication(ComponentA, {
  providers: [
    { provide: APP_ID, useValue: 'app-a' },
    // ... other providers ...
  ]
});

bootstrapApplication(ComponentB, {
  providers: [
    { provide: APP_ID, useValue: 'app-b' },
    // ... other providers ...
  ]
});
```

By default, when there is only one application bootstrapped, you don't need to provide the [`APP_ID`](app_id) token (the `ng` will be used as an app ID).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/APP_ID>
