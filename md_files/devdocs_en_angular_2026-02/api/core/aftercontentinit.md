# AfterContentInit

AfterContentInit



# AfterContentInit

A lifecycle hook that is called after Angular has fully initialized all content of a directive. It will run only once when the projected content is initialized. Define an `ngAfterContentInit()` method to handle any additional initialization tasks.

[OnInit](oninit)[AfterViewInit](afterviewinit)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface AfterContentInit {
  ngAfterContentInit(): void;
}
```

### ngAfterContentInit

`void`

A callback method that is invoked immediately after Angular has completed initialization of all of the directive's content. It is invoked only once when the directive is instantiated.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own content initialization method.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements AfterContentInit {
        ngAfterContentInit() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/AfterContentInit>
