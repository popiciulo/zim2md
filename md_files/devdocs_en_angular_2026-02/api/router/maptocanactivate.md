# mapToCanActivate

mapToCanActivate



# mapToCanActivate

Maps an array of injectable classes with canActivate functions to an array of equivalent [`CanActivateFn`](canactivatefn) for use in a [`Route`](route) definition.

[Route](route)

## API

```
function mapToCanActivate(providers: Type<CanActivate>[]): CanActivateFn[];
```

### mapToCanActivate

`CanActivateFn[]`

Maps an array of injectable classes with canActivate functions to an array of equivalent [`CanActivateFn`](canactivatefn) for use in a [`Route`](route) definition.

Usage {@example router/utils/functional\_guards.ts region='CanActivate'}

@paramproviders`Type<CanActivate>[]`

@returns`CanActivateFn[]`

## Description

Maps an array of injectable classes with canActivate functions to an array of equivalent [`CanActivateFn`](canactivatefn) for use in a [`Route`](route) definition.

Usage

```
@Injectable({providedIn: 'root'})
export class AdminGuard {
  canActivate() {
    return true;
  }
}

const route: Route = {
  path: 'admin',
  canActivate: mapToCanActivate([AdminGuard]),
};
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/mapToCanActivate>
