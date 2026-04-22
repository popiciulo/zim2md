# Title

Title



# Title

A service that can be used to get and set the title of a current HTML document.

## API

```
class Title {
  constructor(_doc: any): Title;
  getTitle(): string;
  setTitle(newTitle: string): void;
}
```

### constructor

`Title`

@param\_doc`any`

@returns`Title`

### getTitle

`string`

Get the title of the current HTML document.

@returns`string`

### setTitle

`void`

Set the title of the current HTML document.

@paramnewTitle`string`

@returns`void`

## Description

A service that can be used to get and set the title of a current HTML document.

Since an Angular application can't be bootstrapped on the entire HTML document (`<html>` tag) it is not possible to bind to the `text` property of the `HTMLTitleElement` elements (representing the `<title>` tag). Instead, this service can be used to set and get the current title value.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/Title>
