# mapToResolve

mapToResolve



# mapToResolve

Maps an injectable class with a resolve function to an equivalent [`ResolveFn`](resolvefn) for use in a [`Route`](route) definition.

[Route](route)

## API

```
function mapToResolve<T>(provider: Type<Resolve<T>>): ResolveFn<T>;
```

### mapToResolve

`ResolveFn<T>`

Maps an injectable class with a resolve function to an equivalent [`ResolveFn`](resolvefn) for use in a [`Route`](route) definition.

Usage {@example router/utils/functional\_guards.ts region='Resolve'}

@paramprovider`Type<Resolve<T>>`

@returns`ResolveFn<T>`

## Description

Maps an injectable class with a resolve function to an equivalent [`ResolveFn`](resolvefn) for use in a [`Route`](route) definition.

Usage

```
@Injectable({providedIn: 'root'})
export class ResolveUser {
  resolve() {
    return {name: 'Bob'};
  }
}

const userRoute: Route = {
  path: 'user',
  resolve: {
    user: mapToResolve(ResolveUser),
  },
};
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/mapToResolve>
