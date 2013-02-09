class User < ActiveRecord::Base
  attr_accessible :first_name, :last_name, :email, :password
  has_and_belongs_to_many :projects
  has_many :tickets

  validates_presence_of :password

  validates :first_name,
            :presence => true,
            :length => { :in => 2..20, :allow_blank => true }

  validates :last_name,
            :presence => true,
            :length => { :in => 2..20, :allow_blank => true }

  validates :email,
            :presence => true,
            :uniqueness => true

  validates_format_of :email, 
                      :with => /^(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i
end