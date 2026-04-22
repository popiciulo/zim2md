# ResolveFn

ResolveFn



# ResolveFn

Function type definition for a data provider.

[Route](route)[Data resolvers](../../guide/routing/data-resolvers)

## API

```
type ResolveFn<T> = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => MaybeAsync<T | RedirectCommand>
```

## Description

Function type definition for a data provider.

A data provider can be used with the router to resolve data during navigation. The router waits for the data to be resolved before the route is finally activated.

A resolver can also redirect a [`RedirectCommand`](redirectcommand) and the Angular router will use it to redirect the current navigation to the new destination.

## Usage Notes

The following example implements a function that retrieves the data needed to activate the requested route.

```
interface Hero {
  name: string;
}
@Injectable()
export class HeroService {
  getHero(id: string) {
    return {name: `Superman-${id}`};
  }
}

export const heroResolver: ResolveFn<Hero> = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => {
  return inject(HeroService).getHero(route.paramMap.get('id')!);
};

bootstrapApplication(App, {
  providers: [
    provideRouter([
      {
        path: 'detail/:id',
        component: HeroDetailComponent,
        resolve: {hero: heroResolver},
      },
    ]),
  ],
});
```

And you can access to your resolved data from `HeroComponent`:

```
@Component({template: ''})
export class HeroDetailComponent {
  private activatedRoute = inject(ActivatedRoute);

  ngOnInit() {
    this.activatedRoute.data.subscribe(({hero}) => {
      // do something with your resolved data ...
    });
  }
}
```

If resolved data cannot be retrieved, you may want to redirect the user to a new page instead:

```
export const heroResolver: ResolveFn<Hero> = async (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot,
) => {
  const router = inject(Router);
  const heroService = inject(HeroService);
  try {
    return await heroService.getHero(route.paramMap.get('id')!);
  } catch {
    return new RedirectCommand(router.parseUrl('/404'));
  }
};
```

When both guard and resolvers are specified, the resolvers are not executed until all guards have run and succeeded. For example, consider the following route configuration:

```
{
 path: 'base'
 canActivate: [baseGuard],
 resolve: {data: baseDataResolver}
 children: [
  {
    path: 'child',
    canActivate: [childGuard],
    component: ChildComponent,
    resolve: {childData: childDataResolver}
   }
 ]
}
```

The order of execution is: baseGuard, childGuard, baseDataResolver, childDataResolver.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ResolveFn>
