# Directive

Directive



# Directive

Decorator that marks a class as an Angular directive. You can define your own directives to attach custom behavior to elements in the DOM.

## API

```
@Directive({
  selector?: string | undefined;
  inputs?:
    | (
        | string
        | {
            name: string;
            alias?: string | undefined;
            required?: boolean | undefined;
            transform?: ((value: any) => any) | undefined;
          }
      )[]
    | undefined;
  outputs?: string[] | undefined;
  providers?: Provider[] | undefined;
  exportAs?: string | undefined;
  queries?: { [key: string]: any } | undefined;
  host?: { [key: string]: string } | undefined;
  jit?: true | undefined;
  standalone?: boolean | undefined;
  hostDirectives?:
    | (
        | Type<unknown>
        | {
            directive: Type<unknown>;
            inputs?: string[] | undefined;
            outputs?: string[] | undefined;
          }
      )[]
    | undefined;
})
```

## Description

Decorator that marks a class as an Angular directive. You can define your own directives to attach custom behavior to elements in the DOM.

The options provide configuration metadata that determines how the directive should be processed, instantiated and used at runtime.

Directive classes, like component classes, can implement [life-cycle hooks](../../guide/components/lifecycle) to influence their configuration and behavior.

## Usage Notes

To define a directive, mark the class with the decorator and provide metadata.

```
import {Directive} from '@angular/core';

@Directive({
  selector: 'my-directive',
})
export class MyDirective {
...
}
```

### Declaring directives

By default, directives are marked as [standalone](../../guide/components/anatomy-of-components#using-components), which makes them available to other components in your application.

```
@Directive({
  selector: 'my-directive',
})
```

Please make sure that directives marked as standalone are not already declared in an NgModule.

\*\* Declaring a directive in an NgModule \*\* If you want to declare a directive in an ngModule, add the `standalone: false` flag to the Directive decorator metadata and add the directive to the `declarations` and `exports` fields of your ngModule.

```
@Directive({
  standalone: false,
  selector: 'my-directive',
})
class MyDirective {}

@NgModule({
  declarations: [MyDirective, SomeComponent],
  exports: [MyDirective], // making it available outside of this module
})
class SomeNgModule {}
```

When declaring a directive in an NgModule, please make sure that:

- the directive is declared in exactly one NgModule.
- the directive is not standalone.
- you do not re-declare a directive imported from another module.
- the directive is included into the `exports` field as well if you want this directive to be accessible for components outside of the NgModule.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Directive>
