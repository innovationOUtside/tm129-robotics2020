# -*- encoding: utf-8 -*-
# stub: guard-jekyll-plus 2.0.2 ruby lib

Gem::Specification.new do |s|
  s.name = "guard-jekyll-plus".freeze
  s.version = "2.0.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Brandon Mathis".freeze]
  s.date = "2015-05-07"
  s.description = "A Guard plugin for smarter Jekyll watching".freeze
  s.email = ["brandon@imathis.com".freeze]
  s.homepage = "http://github.com/imathis/guard-jekyll-plus".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.1.2".freeze
  s.summary = "A Guard plugin for Jekyll which intelligently handles changes to static and template files, only running a Jekyll build when necessary.".freeze

  s.installed_by_version = "3.1.2" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<guard>.freeze, ["~> 2.10", ">= 2.10.3"])
    s.add_runtime_dependency(%q<guard-compat>.freeze, ["~> 1.1"])
    s.add_runtime_dependency(%q<jekyll>.freeze, [">= 1.0.0"])
    s.add_development_dependency(%q<rake>.freeze, [">= 0"])
    s.add_development_dependency(%q<rspec>.freeze, ["~> 3.1"])
    s.add_development_dependency(%q<nenv>.freeze, ["~> 0.1"])
    s.add_development_dependency(%q<bundler>.freeze, [">= 0"])
  else
    s.add_dependency(%q<guard>.freeze, ["~> 2.10", ">= 2.10.3"])
    s.add_dependency(%q<guard-compat>.freeze, ["~> 1.1"])
    s.add_dependency(%q<jekyll>.freeze, [">= 1.0.0"])
    s.add_dependency(%q<rake>.freeze, [">= 0"])
    s.add_dependency(%q<rspec>.freeze, ["~> 3.1"])
    s.add_dependency(%q<nenv>.freeze, ["~> 0.1"])
    s.add_dependency(%q<bundler>.freeze, [">= 0"])
  end
end
