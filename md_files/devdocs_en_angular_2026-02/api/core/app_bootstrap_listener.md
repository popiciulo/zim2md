# APP_BOOTSTRAP_LISTENER

APP\_BOOTSTRAP\_LISTENER



# APP\_BOOTSTRAP\_LISTENER

A DI token that provides a set of callbacks to be called for every component that is bootstrapped.

## API

```
const APP_BOOTSTRAP_LISTENER: InjectionToken<readonly ((compRef: ComponentRef<any>) => void)[]>;
```

## Description

A DI token that provides a set of callbacks to be called for every component that is bootstrapped.

Each callback must take a [`ComponentRef`](componentref) instance and return nothing.

`(componentRef: ComponentRef) => void`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/APP_BOOTSTRAP_LISTENER>
