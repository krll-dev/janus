package de.krll.janus.api;

import org.junit.jupiter.api.Test;
import org.springframework.modulith.core.ApplicationModules;
import org.springframework.modulith.docs.Documenter;

/**
 * Verifiziert, dass die Janus-API modular aufgebaut ist und die Abhängigkeiten
 * zwischen den Modulen korrekt sind. Außerdem wird eine Dokumentation der
 * Module erstellt.
 */
class ModularityTests {

  static final ApplicationModules modules = ApplicationModules.of(JanusApiApplication.class);

  @Test
  void verifiesModuleStructure() {
    modules.verify();
  }

  @Test
  void writesDocumentation() {
    new Documenter(modules).writeDocumentation();
  }

}
