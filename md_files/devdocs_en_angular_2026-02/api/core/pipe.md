# Pipe

Pipe



# Pipe

Decorator that marks a class as pipe and supplies configuration metadata.

[Pipes](../../guide/templates/pipes)

## API

```
@Pipe({
  name: string;
  pure?: boolean | undefined;
  standalone?: boolean | undefined;
})
```

## Description

Decorator that marks a class as pipe and supplies configuration metadata.

A pipe class must implement the [`PipeTransform`](pipetransform) interface. For example, if the name is "myPipe", use a template binding expression such as the following:

```
{{ exp | myPipe }}
```

The result of the expression is passed to the pipe's `transform()` method.

A pipe must belong to an NgModule in order for it to be available to a template. To make it a member of an NgModule, list it in the `declarations` field of the [`NgModule`](ngmodule) metadata.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Pipe>
