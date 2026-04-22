# generate web-worker

generate web-worker



# generate web-worker

```
ng generate web-worker[name][options]
```

Creates a new web worker in your project. Web workers allow you to run JavaScript code in the background, improving the performance and responsiveness of your application by offloading computationally intensive tasks. This schematic generates the necessary files for a new web worker and provides an optional code snippet to demonstrate its usage.

## Arguments

### name

The name for the new web worker. This will be used to create the worker file (e.g., `my-worker.worker.ts`).

#### Value Type

`string`

## Options

### project

The name of the project where the web worker should be created. If not specified, the CLI will determine the project from the current directory.

#### Value Type

`string`

### snippet

Generate a code snippet that demonstrates how to create and use the new web worker.

#### Value Type

`boolean`

#### Default

`true`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/cli/generate/web-worker>
