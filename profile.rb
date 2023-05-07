require 'json'


class Education
  attr_accessor :course, :institution, :year

  def initialize(course, institution, year)
    @course = course
    @institution = institution
    @year = year
  end

  def description
    "#{course} - #{institution} (#{year})"
  end
end

class Profile
  attr_reader :name
  attr_accessor :education, :skills, :interests

  def initialize(name, github)
    @name = name.upcase!
    @github = github
    @education = []
    @skills = []
    @interests = []
  end

  def github_profile
    "https://github.com/#{@github}"
  end

  def about
    puts "👨 #{name}"
    puts "🌐 Perfil: #{github_profile}"

    puts "\n🎓 Formação:"
    education.each { |e| puts "  - #{e.description}" }

    puts "\n🛠️  Habilidades:"
    skills.each { |s| puts "  - #{s}" }
    
    puts "\n🤩 Interesses:"
    interests.each { |i| puts "  - #{i}" }
  end
end


me = Profile.new('Lucas Sanches', 'sancheslz')

details = open('details.json').read
details = JSON.parse!(details, {symbolize_names: true})

details.each do |category, attributes|
  attributes.each do |attribute|
    if Object.const_defined?(category.capitalize)
      me.send(category) << Object.const_get(category.capitalize).new(*attribute.values)
    else
      me.send(category) << attribute
    end
  end
end

me.about
