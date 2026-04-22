# Resolve

Resolve



# Resolve

Interface that classes can implement to be a data provider. A data provider class can be used with the router to resolve data during navigation. The interface defines a `resolve()` method that is invoked right after the [`ResolveStart`](resolvestart) router event. The router waits for the data to be resolved before the route is finally activated.

[ResolveFn](resolvefn)[Data resolvers](../../guide/routing/data-resolvers)

## API

```
interface Resolve<T> {
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): any;
}
```

### resolve

`any`

@paramroute`ActivatedRouteSnapshot`

@paramstate`RouterStateSnapshot`

@returns`any`

## Description

Interface that classes can implement to be a data provider. A data provider class can be used with the router to resolve data during navigation. The interface defines a `resolve()` method that is invoked right after the [`ResolveStart`](resolvestart) router event. The router waits for the data to be resolved before the route is finally activated.

The following example implements a `resolve()` method that retrieves the data needed to activate the requested route.

```
@Injectable({ providedIn: 'root' })
export class HeroResolver implements Resolve<Hero> {
  constructor(private service: HeroService) {}

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<Hero>|Promise<Hero>|Hero {
    return this.service.getHero(route.paramMap.get('id'));
  }
}
```

Here, the defined `resolve()` function is provided as part of the [`Route`](route) object in the router configuration:

```
@NgModule({
  imports: [
    RouterModule.forRoot([
      {
        path: 'detail/:id',
        component: HeroDetailComponent,
        resolve: {
          hero: HeroResolver
        }
      }
    ])
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

And you can access to your resolved data from `HeroComponent`:

```
@Component({
 selector: "app-hero",
 templateUrl: "hero.component.html",
})
export class HeroComponent {

 constructor(private activatedRoute: ActivatedRoute) {}

 ngOnInit() {
   this.activatedRoute.data.subscribe(({ hero }) => {
     // do something with your resolved data ...
   })
 }

}
```

## Usage Notes

When both guard and resolvers are specified, the resolvers are not executed until all guards have run and succeeded. For example, consider the following route configuration:

```
{
 path: 'base'
 canActivate: [BaseGuard],
 resolve: {data: BaseDataResolver}
 children: [
  {
    path: 'child',
    guards: [ChildGuard],
    component: ChildComponent,
    resolve: {childData: ChildDataResolver}
   }
 ]
}
```

The order of execution is: BaseGuard, ChildGuard, BaseDataResolver, ChildDataResolver.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/Resolve>
