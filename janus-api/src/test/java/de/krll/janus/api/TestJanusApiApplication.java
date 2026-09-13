package de.krll.janus.api;

import org.springframework.boot.SpringApplication;

public class TestJanusApiApplication {

	public static void main(String[] args) {
		SpringApplication.from(JanusApiApplication::main).with(TestcontainersConfiguration.class).run(args);
	}

}
