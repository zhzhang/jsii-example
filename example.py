from jsii_example import Foo, Bar

foo = Foo(name="foo")
reveal_type(foo)
bar = Bar(foo=foo)
reveal_type(bar)
reveal_type(bar.foo)
reveal_type(bar.foo.name)
