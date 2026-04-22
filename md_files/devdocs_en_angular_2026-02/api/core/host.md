# Host

Host



# Host

Parameter decorator on a view-provider parameter of a class constructor that tells the DI framework to resolve the view by checking injectors of child elements, and stop when reaching the host element of the current component.

## API

```
@Host();
```

## Usage Notes

The following shows use with the [`@Optional`](optional) decorator, and allows for a `null` result.

```
class OtherService {}
        class HostService {}

        @Directive({
          selector: 'child-directive',
          standalone: false,
        })
        class ChildDirective {
          logs: string[] = [];

          constructor(@Optional() @Host() os: OtherService, @Optional() @Host() hs: HostService) {
            // os is null: true
            this.logs.push(`os is null: ${os === null}`);
            // hs is an instance of HostService: true
            this.logs.push(`hs is an instance of HostService: ${hs instanceof HostService}`);
          }
        }

        @Component({
          selector: 'parent-cmp',
          viewProviders: [HostService],
          template: '<child-directive></child-directive>',
          standalone: false,
        })
        class ParentCmp {}

        @Component({
          selector: 'app',
          viewProviders: [OtherService],
          template: '<parent-cmp></parent-cmp>',
          standalone: false,
        })
        class App {}
```

For an extended example, see ["Dependency Injection Guide"](../../guide/di/di-in-action#optional).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Host>
