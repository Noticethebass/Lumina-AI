const { Client, GatewayIntentBits, REST, Routes } = require('discord.js');
const { token, clientId, guildId } = require('./config.json');
const fs = require('node:fs');
const path = require('node:path');

// Initialize the client
const client = new Client({ intents: [GatewayIntentBits.Guilds] });

// Store commands in a Map
client.commands = new Map();

// Load command files
const commandsPath = path.join(__dirname, 'commands');
const commandFiles = fs.readdirSync(commandsPath).filter(file => file.endsWith('.js'));

// Register commands for the bot
const commands = [];
for (const file of commandFiles) {
	const command = require(path.join(commandsPath, file));
	client.commands.set(command.data.name, command);
	commands.push(command.data.toJSON());
}

// Register commands with Discord API (for a specific guild)
const rest = new REST({ version: '10' }).setToken(token);

(async () => {
	try {
		console.log('Started refreshing application (/) commands.');

		// Use Guild commands or global commands
		await rest.put(
			Routes.applicationGuildCommands(clientId, guildId),
			{ body: commands },
		);

		console.log('Successfully reloaded application (/) commands.');
	}
	catch (error) {
		console.error('Error registering commands:', error);
	}
})();

// Handle client "ready" event
client.once('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
});

// Handle interactions
client.on('interactionCreate', async interaction => {
	if (!interaction.isCommand()) return;

	const command = client.commands.get(interaction.commandName);

	if (!command) {
		await interaction.reply({ content: 'Command not found.' });
		return;
	}

	try {
		await command.execute(interaction);
	}
	catch (error) {
		console.error(error);
		await interaction.reply({ content: 'There was an error executing the command.' });
	}
});

// Login
client.login(token);
