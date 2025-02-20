const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('fetch')
		.setDescription('Fetchs last message sent in fetch channel'),
	async execute(interaction) {

		// Replys to command (this is necessary)
		await interaction.reply('Fetching the message...');

		try {
    	const channel = interaction.guild.channels.cache.get('1336458642567987232');

    	if (!channel) {
    	console.error('Channel not found.');
    	return interaction.followUp('Channel not found.');
    	}

    	// Fetch
    	const messages = await channel.messages.fetch({ limit: 1 });
    	 const firstMessage = messages.first();

    	if (!firstMessage) {
    	console.error('No messages found in the specified channel.');
    	return interaction.followUp('No messages found in the specified channel.');
    	}

    	// Send
    	await interaction.followUp(`${firstMessage.content}`);
		}
		catch (error) {
    	 // error logging
    	console.error('Error executing the command:', error);
    	await interaction.followUp('There was an error executing the command.');
		}
	},
};