# mapToCanMatch

mapToCanMatch



# mapToCanMatch

Maps an array of injectable classes with canMatch functions to an array of equivalent [`CanMatchFn`](canmatchfn) for use in a [`Route`](route) definition.

[Route](route)

## API

```
function mapToCanMatch(providers: Type<CanMatch>[]): CanMatchFn[];
```

### mapToCanMatch

`CanMatchFn[]`

Maps an array of injectable classes with canMatch functions to an array of equivalent [`CanMatchFn`](canmatchfn) for use in a [`Route`](route) definition.

Usage {@example router/utils/functional\_guards.ts region='CanActivate'}

@paramproviders`Type<CanMatch>[]`

@returns`CanMatchFn[]`

## Description

Maps an array of injectable classes with canMatch functions to an array of equivalent [`CanMatchFn`](canmatchfn) for use in a [`Route`](route) definition.

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
<https://angular.dev/api/router/mapToCanMatch>
