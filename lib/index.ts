export interface Foo {
  readonly name: string;
}

export interface Bar {
  readonly foo: Foo;
}
