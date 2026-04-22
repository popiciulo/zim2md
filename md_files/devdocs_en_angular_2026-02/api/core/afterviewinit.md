# AfterViewInit

AfterViewInit



# AfterViewInit

A lifecycle hook that is called after Angular has fully initialized a component's view. Define an `ngAfterViewInit()` method to handle any additional initialization tasks.

[OnInit](oninit)[AfterContentInit](aftercontentinit)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface AfterViewInit {
  ngAfterViewInit(): void;
}
```

### ngAfterViewInit

`void`

A callback method that is invoked immediately after Angular has completed initialization of a component's view. It is invoked only once when the view is instantiated.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own view initialization method.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements AfterViewInit {
        ngAfterViewInit() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AfterViewInit>
