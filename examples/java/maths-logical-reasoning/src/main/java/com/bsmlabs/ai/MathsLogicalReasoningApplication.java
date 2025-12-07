package com.bsmlabs.ai;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class MathsLogicalReasoningApplication {

	static void main(String[] args) {
		SpringApplication.run(MathsLogicalReasoningApplication.class, args);
	}

    @Bean
    public CommandLineRunner runner(ChatClient.Builder builder) {
        return args -> {
            var chatClient = builder.build();
            String response = chatClient.prompt("what is 2+2").call().content();
            IO.println(response);
        };
    }

}
